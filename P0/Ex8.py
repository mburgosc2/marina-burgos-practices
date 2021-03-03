import P0.Seq0 as Seq0

gene_folder = "./sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("------|EXERCISE 8|------")
for gene in gene_list:
    seq = Seq0.seq_read_fasta(gene_folder + gene + ".txt")
    bases_count = Seq0.seq_count(seq)
    print( "Gene " + gene + ": Most frequent base: " + str(Seq0.max_base(bases_count)))