import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils as su

LIST_SEQUENCES =["AGTCAAAAATTTTCCCCGGGATTACATCAT", "ATGACTAGACATTTTTTTCGCGCGCATAC", "AAAAATTTCCGATACTAGTACGTACTG",
                 "AACGGGGCTTTTCAGCTAC","AAAAAAAAAAAAGGGGGGGGTTTCGCT"]
LIST_GENES = ["U5.txt", "ADA.txt", "FXN.txt", "RNU6_269P.txt", "FRAT1.txt"]


# Define the Server's port
PORT = 8084
HTML_ASSETS = "./html"



information = {
    "A":{"link": "https://en.wikipedia.org/wiki/Adenine",
         "formula": "CH5N5",
          "name": "ADENINE",
         "color": "lightgreen"
        },
    "C": {"link": "https://en.wikipedia.org/wiki/Cytosine",
          "formula": "C4H5N3O",
          "name": "CYTOSINE",
          "color": "lightyellow"
          },
    "G": {"link": "https://en.wikipedia.org/wiki/Guanine",
          "formula": "C5H5N5O",
          "name": "GUANINE",
          "color": "lightskyblue"
          },
    "T": {"link": "https://en.wikipedia.org/wiki/Thymine",
          "formula": "C5H6N2O2",
          "name": "THYMINE",
          "color": "lightpink"
          }

}


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested:", path_name)
        print("Parameters:", arguments)


        context = {}
        if path_name == "/":
            context["n_seq"] = len(LIST_SEQUENCES)
            context["list_genes"] = LIST_GENES
            contents = su.read_template_html_file("./html/index.html").render(context=context)
        elif path_name == "/test":
            contents = su.read_template_html_file("./html/test.html").render()
        elif path_name== "/ping":
            contents = su.read_template_html_file("./html/ping.html").render()
        elif path_name== "/get":
            number_seq = arguments["sequence"][0]
            contents = su.get(LIST_SEQUENCES, number_seq)
        elif path_name == "/gene":
            gene = arguments["gene"][0]
            contents = su.genes(gene)
        elif path_name =="/operation":
            sequence = arguments["sequence"][0]
            operation = arguments["calculation"][0]
            if operation =="Rev":
                contents = su.reverse(sequence)
            elif operation == "Info":
                contents = su.bases(sequence)
            elif operation == "Comp":
                contents = su.complement(sequence)
        else:
            contents = su.read_template_html_file("./html/ERROR.html").render()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()