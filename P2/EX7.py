from Client0 import Client
from pathlib import Path
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8083
PORT2 = 12300

# -- Create a client object
c = Client(IP, PORT)
c2 = Client(IP, PORT2)

s = Seq()
s.read_fasta("FRAT1.txt")
count = 0
i = 0
while i < len(s.strbases) and count < 10:
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    print("Fragment", count, ":", fragment)
    if count % 2 == 0:
        print(c2.talk("Fragment" + str(count) + ":" + fragment))
    else:
        print(c.talk("Fragment" + str(count) + ":" + fragment))