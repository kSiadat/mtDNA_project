import matplotlib.pyplot as plt
from subSeq import subSeq

def write_file(genome, window, path):
    '''Creates a text file for circos containing the data needed to plot a line plot of the proportions of a base'''
    bases = list(set(genome))
    if "N" in bases:
        del bases[bases.index("N")]
    bases.sort()

    fractions = [[subSeq(i,window,genome).count(base)/(2*window + 1) for i in range(len(genome))] for base in bases]

    for b in range(len(fractions)):
        text = ""
        for f in range(len(fractions[b])):
            if not (fractions[b][f]==fractions[b][f-1] and fractions[b][f]==fractions[b][(f+1)%len(fractions[b])]):
                text += f"mt1 {f} {f} {fractions[b][f]}\n"
        file = open(f"{path}_{window}_{bases[b]}.txt", "w+")
        file.write(text)
        file.close()

path1 = "..\\..\\data\\mtDNA.fa"
path2 = "..\\..\\data\\bases"

file = open(path1,"r")
lines = [l.rstrip() for l in file.readlines()]
file.close()
genome = "".join(lines[1:])
print(len(genome))

write_file(genome, 10, path2)
write_file(genome, 100, path2)
write_file(genome, 500, path2)
