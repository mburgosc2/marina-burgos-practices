from pathlib import Path

def seq_ping():
    print("OK")

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







