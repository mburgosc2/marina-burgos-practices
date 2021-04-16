from Seq1 import Seq
from Client0 import Client

print("----| PRACTICE 3, EXERCISE 7 |----")

c = Client("127.0.0.1", 8081)
print(c)

print(" * TESTING PING...")

response = c.talk("PING")
print(response)


print("\n" +" * TESTING GET...")

for i in range(0,5):
    a = (c.talk("GET "+ str(i)))
    print(a)

print( " * TESTING INFO... ")
print(c.talk("INFO AGTCAAAAATTTTCCCCGGGATTACATCAT"))
print("\n" +" * TESTING COMP... ")
print(c.talk("COMP AGTCAAAAATTTTCCCCGGGATTACATCAT"))
print("\n" +" * TESTING REV... ")
print(c.talk("REV AGTCAAAAATTTTCCCCGGGATTACATCAT"))


print("\n" + " * TESTING GENE... ")
print(c.talk("GENE U5") + "\n")
print(c.talk("GENE ADA")+ "\n")
print(c.talk("GENE FRAT1")+ "\n")
print(c.talk("GENE RNU6_269P")+ "\n")
print(c.talk("GENE FXN")+ "\n")










