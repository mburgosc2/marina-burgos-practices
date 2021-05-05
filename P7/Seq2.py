
import termcolor
from pathlib import Path

class Seq:
    """A class for representing sequences"""
    NULL_SEQ = "NULL"
    INVALID_SEQ = "ERROR"

    def __init__(self, strbases = NULL_SEQ):
        # Initialize the sequence with the value
        # passed as argument when creating the object

        if strbases == Seq.NULL_SEQ :
            print("NULL Seq created!")
            self.strbases = strbases
        else:
            if Seq.is_valid_sequence2(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQ
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
        if self.strbases == Seq.NULL_SEQ or self.strbases == Seq.INVALID_SEQ:
            return 0
        else:
            return len(self.strbases)


    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if not self.strbases == Seq.NULL_SEQ and not(self.strbases == Seq.INVALID_SEQ):
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                elif ch == "T":
                    t += 1
        return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        dict_bases = {"A" : a, "C" : c, "G" : g, "T" : t}
        return dict_bases

    def reverse(self):
        if self.strbases == Seq.NULL_SEQ:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQ:
            return "ERROR"
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQ:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQ:
            return "ERROR"
        else:
            complement = ""
            for ch in self.strbases:
                if ch == "A":
                    complement += "T"
                elif ch == "C":
                    complement += "G"
                elif ch == "G":
                    complement += "C"
                elif ch == "T":
                    complement += "A"
            return complement

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    # def read_fasta(self, filename)



    def read_fasta2(self, filename):
        seq = Path(filename).read_text()
        seq = seq[seq.find("\n") + 1:].replace("\n", "")
        self.strbases = seq

        return self.strbases

    def percentage_base(self, count_bases, seq_len):
        a = str(round(count_bases[0] / seq_len * 100, 2)) + "%"
        c = str(round(count_bases[1] / seq_len * 100, 2)) + "%"
        g = str(round(count_bases[2] / seq_len * 100, 2)) + "%"
        t = str(round(count_bases[3] / seq_len * 100, 2)) + "%"
        return {"A": a, "C":c, "G":g, "T":t}

    @staticmethod
    def max_dict(dict_count):
        return max(dict_count, key=dict_count.get)

















def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("jskdhs")
    return s1, s2, s3








