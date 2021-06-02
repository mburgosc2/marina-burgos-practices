
import http.client
import http.server
import socketserver
import termcolor
from jinja2 import Template
from pathlib import Path
import json
from urllib.parse import urlparse, parse_qs
import server_utils


# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("RESOURCE REQUESTED: ", path_name)
        print("PARAMETERS: ", arguments)
        context = {}
        if path_name == "/":
            contents = server_utils.read_template_html_file("./html/index.html").render(context=context)
        elif path_name == "/listSpecies":
            dict_s = server_utils.get_data("/info/species")
            if len(arguments) == 1:
                try:
                    limit = arguments["limit"][0]

                except KeyError:
                    limit = len(dict_s["species"])
                contents = server_utils.list_species(dict_s, limit)

            else:
                contents = server_utils.read_template_html_file("./html/ERROR.html").render()
        elif path_name == "/karyotype":
            if len(arguments) == 1:
                try:
                    specie_name = arguments["specie"][0]
                    dict_k = server_utils.get_data("info/assembly" + "/" + specie_name)
                    contents = server_utils.karyotype(dict_k, specie_name)
                except KeyError:
                    contents = server_utils.read_template_html_file("./html/ERROR.html").render()
                except ValueError:
                    contents = server_utils.read_template_html_file("./html/ERROR.html").render()
            else:
                contents = server_utils.read_template_html_file("./html/ERROR.html").render()

        elif path_name == "/chromosomeLength":
            if len(arguments) == 2:
                try:
                    specie= arguments["specie"][0]
                    chromo = arguments["chromo"][0]
                    dict_c = server_utils.get_data("/info/assembly" + "/" + specie + "/" + chromo )
                    contents = server_utils.length_chromosome(dict_c, specie, chromo)
                except KeyError:
                    contents = server_utils.read_template_html_file("./html/ERROR.html").render()
                except ValueError:
                    contents = server_utils.read_template_html_file("./html/ERROR.html").render()
            else:
                contents = server_utils.read_template_html_file("./html/ERROR.html").render()

        elif path_name == "/geneSeq":
            if len(arguments) == 1:
                try:
                    gene = arguments["gene"][0]
                    dict_seq = server_utils.get_data("/sequence/id/" + server_utils.genes_dict[gene])
                    contents = server_utils.sequence(dict_seq, gene)
                except KeyError:
                    contents = server_utils.read_template_html_file("./html/ERROR.html").render()
                except ValueError:
                    contents = server_utils.read_template_html_file("./html/ERROR.html").render()
            else:
                contents = server_utils.read_template_html_file("./html/ERROR.html").render()
        elif path_name == "/geneInfo":
            if len(arguments) == 1:
                try:
                    gene = arguments["gene"][0]
                    dict_info = server_utils.get_data("/sequence/id/" + server_utils.genes_dict[gene])
                    contents = server_utils.infoseq(dict_info, gene)
                except KeyError:
                    contents = server_utils.read_template_html_file("./html/ERROR.html").render()
                except ValueError:
                    contents = server_utils.read_template_html_file("./html/ERROR.html").render()
            else:
                contents = server_utils.read_template_html_file("./html/ERROR.html").render()
        elif path_name == "/geneCalc":
            if len(arguments) == 1:
                try:
                    gene = arguments["gene"][0]
                    dict_calc = server_utils.get_data("/sequence/id/" + server_utils.genes_dict[gene])
                    contents = server_utils.calcseq(dict_calc, gene)
                except KeyError:
                    contents = server_utils.read_template_html_file("./html/ERROR.html").render()
                except ValueError:
                    contents = server_utils.read_template_html_file("./html/ERROR.html").render()
            else:
                contents = server_utils.read_template_html_file("./html/ERROR.html").render()

        else:
            contents = server_utils.read_template_html_file("./html/ERROR.html").render()

        self.send_response(200)
        length = len(contents.encode())
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(length))
        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(str.encode(contents))
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
        print("Stopped by the user")
        httpd.server_close()

