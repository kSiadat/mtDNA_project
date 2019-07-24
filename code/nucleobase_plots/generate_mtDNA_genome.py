import random as rn

genome = "\n"
bases = ["A", "C", "G", "T"]
for b in range(16569):
    genome += bases[rn.randint(0, len(bases)-1)]

file = open("../data/mtDNA_random.fa", "w+")
file.write(genome)
file.close()
