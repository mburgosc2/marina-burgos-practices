import P0.Seq0 as Seq0
FOLDER = "./sequences/"
id = "U5.txt"
U5_seq = Seq0.seq_read_fasta(FOLDER + id)
print("The first 20 bases are: ", U5_seq[0:20])


