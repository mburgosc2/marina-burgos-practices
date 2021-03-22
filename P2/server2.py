import socket

# Configure the Server's IP and PORT
PORT = 12300 #(you can not have 2 applications using the = port)
IP = "127.0.0.1" #127.0.0.1 (local one)
MAX_OPEN_REQUESTS = 5

# COUNTING NUMBER CONNECTIONS
number_con = 0

#CREATE AN INET, STREAMING SOCKET
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    #become a server socket
    #MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        #accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        #another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        # Send the message
        message = "Hello from the teacher's server"
        # We must write bytes, not a string
        clientsocket.send(message.encode())
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()

