def correct_seq(dna):
    for ch in dna:
        if ch != "A" and ch != "C" and ch != "G" and ch != "T":
            return False

    return True



def count_bases(dna):
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

dna = input("Introduce the sequence: ")
correct_dna = correct_seq(dna)
if correct_dna:
    print("Total length: " + str(len(dna)))
    a, c, g, t = count_bases(dna)
    print("A:", a)
    print("C:", c)
    print("G:", g)
    print("T:", t)

else:
    print("Not a valid dna seq")