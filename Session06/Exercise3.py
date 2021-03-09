import Session06.Seq0 as Seq0
from Session06.Seq0 import Seq

seq_list1 = Seq0.generate_seqs("A", 3)
seq_list2 = Seq0.generate_seqs("AC", 5)

print("list 1:")
Seq.print_seqs(seq_list1)


print()
print("list 2:")
Seq.print_seqs(seq_list2)