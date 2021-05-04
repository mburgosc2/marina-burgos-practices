import Seq1
from Seq1 import Seq
from pathlib import Path
from jinja2 import Template


def read_template_html_file(filename):
    contents = Template(Path(filename).read_text())
    return contents



def print_color(message, color):
    import termcolor
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping(cs):
    print_color("PING COMMAND!", "green")
    cs.send(str("OK!").encode())

def get(list_Sequences, argument):
    print_color("GET", "yellow")
    context = {
        "number": argument,
        "sequence": list_Sequences[int(argument)]}
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents

def bases(sequence):
    print_color("INFO", "yellow")
    seq = Seq(sequence)
    counting_bases =""

    for base, number_of_bases in seq.count().items():
            info = str(base) + ": " + str(number_of_bases) + " " + "(" + str(round(number_of_bases / len(sequence) * 100, 1)) + "%"+ ")" + "\n"
            counting_bases += info
    context = {
        "sequence": sequence,
        "operation": "Info",
        "result": "Total length: " + str(len(sequence)) + "   " + "\n" + str(counting_bases)
    }
    contents = read_template_html_file("./html/operations.html").render(context=context)
    return contents





def complement(sequence):
    print_color("COMP", "yellow")
    seq = Seq(sequence)
    context = {
        "sequence": sequence,
        "operation": "Comp",
        "result": seq.complement()
    }
    contents = read_template_html_file("./html/operations.html").render(context=context)
    return contents

def reverse(sequence):
    print_color("REV", "yellow")
    seq = Seq(sequence)
    context = {
        "sequence": sequence,
        "operation": "Rev",
        "result": seq.reverse()
    }
    contents = read_template_html_file("./html/operations.html").render(context=context)
    return contents


def genes(argument):
    print_color("GENE", "yellow")
    PATH = "./sequences/" + argument
    seq = Seq()
    seq.read_fasta2(PATH)
    context = {
        "gene_name": argument,
        "gene_contents": seq.strbases
    }
    contents =read_template_html_file("./html/gene.html").render(context=context)
    return contents
