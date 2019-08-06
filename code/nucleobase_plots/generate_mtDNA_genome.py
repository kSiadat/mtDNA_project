import random as rn

path="..\..\data\mtDNA.fa"

file = open(path, "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()
genome = list("".join(lines[1:]))

for f in range(3):
    rnGenome = genome[:]
    rn.shuffle(rnGenome)
    rnGenome = "\n" + "".join(rnGenome)
    file = open(f"../../data/mtDNA_random_{f+1}.fa", "w+")
    file.write(rnGenome)
    file.close()
