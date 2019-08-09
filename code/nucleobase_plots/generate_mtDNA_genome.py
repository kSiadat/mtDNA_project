import random as rn

path="..\..\data\mtDNA.fa"

file = open(path, "r")
genome = list(file.read())
file.close()

for f in range(3):
    rnGenome = genome[:]
    rn.shuffle(rnGenome)
    rnGenome = "".join(rnGenome)
    file = open(f"../../data/mtDNA_random_{f+1}.fa", "w+")
    file.write(rnGenome)
    file.close()
