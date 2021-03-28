from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8083

# -- Create a client object
c = Client(IP, PORT)
response = c.talk("Message for u <3")
print("Response:", response)