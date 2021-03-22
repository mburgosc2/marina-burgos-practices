from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8083

# -- Create a client object
c = Client(IP, PORT)
print(c.talk("Sending the U5 gene to the server..."))
print(c.talk(Path("U5.txt").read_text()))