from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8083

c = Client(IP, PORT)
print(c.debug_talk("MESSAGE 1----"))
print(c.debug_talk("MESSAGE 2: TESTING !!!"))
