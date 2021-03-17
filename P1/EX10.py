from Seq1 import Seq


gene_folder = "./sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

def print_result(seq):
    print("Gene " + str(gene) + ": Most frequent base: " + str(Seq.max_dict(seq.count())))

print("------|EXERCISE 10|------")

for gene in gene_list:
    s1 = Seq()
    s1.read_fasta(gene_folder + gene + ".txt")
    bases_count = Seq.count(s1)
    print_result(s1)