import Seq1
from Seq1 import Seq
from pathlib import Path


def print_color(message, color):
    import termcolor
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping(cs):
    print_color("PING COMMAND!", "green")
    cs.send(str("OK!").encode())

def get(cs, list_Sequences, argument):
    print_color("GET", "yellow")
    response = list_Sequences[int(argument)]
    print(response)
    cs.send(str(response).encode())

def bases(cs, argument):
    print_color("INFO", "yellow")
    seq = Seq(argument)
    counting_bases =""

    for base, number_of_bases in seq.count().items():
            info = str(base) + ": " + str(number_of_bases) + " " + "(" + str(round(number_of_bases / len(argument) * 100, 1)) + "%"+ ")" + "\n"
            counting_bases += info
    response = "Sequence: " + str(argument) + "\n" "Length: " + str(len(argument)) + "\n" + str(counting_bases)
    # print("Sequence: " + str(argument) + "\n" + "Total length: " +  str(len(argument)) + "\n" + str(seq.count()))
    print(response)
    cs.send(str(response).encode())



def complement(cs, argument):
    print_color("COMP", "yellow")
    seq = Seq(argument)
    print(seq.complement())
    response  = seq.complement()
    cs.send(str(response).encode())

def reverse(cs, argument):
    print_color("REV", "yellow")
    seq = Seq(argument)
    print(seq.reverse())
    response = seq.reverse()
    cs.send(str(response).encode())

def genes(cs, argument):
    print_color("GENE", "yellow")
    seq = Seq()
    response = str(seq.read_fasta2(argument + ".txt"))
    print(response)
    cs.send(response.encode())

    #print(seq.read_fasta(filename))