import random

path="..\..\data\mtDNA.fa" # accession number instead?
Nshuffle = 3
outpaths = [f"../../data/mtDNA_random_{f+1}.fa" for f in range(Nshuffle)]

file = open(path, "r")
genome = list(file.read())
file.close()

rnGenome = genome[:]
for f in range(Nshuffle):
    random.shuffle(rnGenome)
    rnGenstr = "".join(rnGenome)
    file = open(outpaths[f], "w+") # accession numbe filename
    file.write(rnGenstr)
    file.close()
