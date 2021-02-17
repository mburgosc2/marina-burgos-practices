def correct_seq(dna):
    for ch in dna:
        if ch != "A" and ch != "C" and ch != "G" and ch != "T":
            return False

    return True





def count(dna):
    a, c, g, t = 0, 0, 0, 0
    for i in dna:
        if i == "A":
            a += 1
        elif i == "C":
            c += 1
        elif i == "G":
            g += 1
        elif i == "T":
            t += 1
    return a, c, g, t

def read_from_file(filename):
    with open(filename, "r") as f:
        dna = f.read()
        dna = dna.replace("\n", "")

        return dna


dna = read_from_file("dna.txt")
if correct_seq(dna):
    print("Total length: ", len(dna))
    a, c, g, t = count(dna)
    print("A", a)
    print("C", c)
    print("G", g)
    print("T", t)
else:
    print("Not a valid sequence")