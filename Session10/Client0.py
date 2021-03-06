import socket
from termcolor import cprint, colored

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self): #ping to test if a webpg works
        print("OK")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up")
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running? Have you checked the IP and the Port?")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        print("To Server:", msg)
        s.send(msg.encode())
        # Receive data
        response = s.recv(2048).decode("utf-8")
        # Close the socket
        s.close()
        # Return the response
        return "From server: " + response

    def debug_talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        print("To Server:", colored(msg, 'blue'))
        s.send(msg.encode())
        # Receive data
        response = colored(s.recv(2048).decode("utf-8"), 'yellow')
        print("From Server:", response)
        # Close the socket
        s.close()
        # Return the response
        return "From server: " + response
