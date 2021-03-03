import P0.Seq0 as Seq0
FOLDER = "./sequences/"
id = "U5.txt"
U5_seq = Seq0.seq_read_fasta(FOLDER + id)
print("------|EXERCISE 7|------")
print("Gene U5:")
U5_seq_correct = U5_seq[0:20]
print("Frag: ", U5_seq_correct)
print("Rev:", Seq0.seq_complement(U5_seq_correct))