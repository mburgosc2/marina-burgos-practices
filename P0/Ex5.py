import P0.Seq0 as Seq0

gene_folder = "./sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("------|EXERCISE 5|------")
for gene in gene_list:
    seq = Seq0.seq_read_fasta(gene_folder + gene + ".txt")
    print( "Gene " + gene + ": " + str(Seq0.seq_count(seq)))