import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8084

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        print(self.path)

        if self.path == "/":
            contents = Path("form-EX01.html").read_text()
        elif self.path.startswith("/echo?msg"):
            message = self.path.split("?msg=")[1]
            print("Message is", message)
            contents = Path("template.html").read_text().format(message).replace("+", " ")
        else:
            contents = Path("ERROR.html").read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
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
        print("Stoped by the user")
        httpd.server_close()