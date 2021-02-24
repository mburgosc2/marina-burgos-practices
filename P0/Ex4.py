import P0.Seq0 as Seq0
gene_folder = "./sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "T", "G"]

print("------|EXERCISE 4|------")
for gene in gene_list:
    seq = Seq0.seq_read_fasta(gene_folder + gene + ".txt")
    print("Gene", gene)
    for base in base_list:
        print(base + ": " + str(Seq0.seq_count_base(seq, base)))


