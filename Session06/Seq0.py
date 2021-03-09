from pathlib import Path
import termcolor

def seq_ping():
    print("OK")

def is_valid_sequence(strbases):
    for c in strbases:
        if c != "A" and c!="C" and c != "G" and c != "T":
            return False
    return True

def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")

def seq_read_fasta(filename):
    return take_out_first_line(Path(filename).read_text())

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    gene_dict = {"A":0, "C":0, "G":0, "T":0}
    for i in seq:
         gene_dict[i] += 1
    return gene_dict

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):

    rev = ""
    complement_bases = {"A": "T", "C": "G", "G":"C" , "T": "A"}
    for i in seq:
        if i in complement_bases:
            rev += complement_bases[i]
        else:
            rev += i
    return rev

import math

def max_base(seq_count):
    return max(seq_count, key=seq_count.get)


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.is_valid_sequence():
            print("New sequence created!")

        else:
            self.strbases = "ERROR"
            print("INCORRECT Sequence detected")

    @staticmethod
    def is_valid_sequence2(bases):
        for c in bases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True


    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c!="C" and c != "G" and c != "T":
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = "Sequence" + str(i) + ": (Length:" + str(list_sequences[i].len()) + ")" + str(list_sequences[i])
            termcolor.cprint(text, "yellow")


    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


def generate_seqs(pattern, number):
    list_seq =[]
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))

    return list_seq


# main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("ujhfdjh")

# printing objects
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")









