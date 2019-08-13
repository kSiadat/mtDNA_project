from mtdna_utilities import get_genome, subSeq, write_file
import matplotlib.pyplot as plt


def calc_fractions(genome, window):
    '''Calculates the fractions required to plot nucleobase proportions'''
    bases = list(set(genome))
    if "N" in bases:
        del bases[bases.index("N")]
    bases.sort()
    fractions = [[subSeq(i,window,genome).count(base)/(2*window + 1) for i in range(len(genome))] for base in bases]
    return fractions, bases


def write_plotData(accession, path, fractions, bases, window):
    '''Creates the file needed for circos to create a line plot'''
    for b in range(len(fractions)):
        text = ""
        for f in range(len(fractions[b])):
            if not (fractions[b][f]==fractions[b][f-1] and fractions[b][f]==fractions[b][(f+1)%len(fractions[b])]):
                text += f"mt1 {f} {f} {fractions[b][f]}\n"
        write_file(f"{path}{accession}_linePlot_{window}_{bases[b]}.txt", text)


accession = "NC_012920.1"
path = "../data/"

genome = get_genome(accession)
print(f"Length of genome: {len(genome)}")
windows = [10, 100, 500]

for x in range(len(windows)):
    fractions, bases = calc_fractions(genome, windows[x])
    write_plotData(accession, path, fractions, bases, windows[x])
    print(f"Completed window {windows[x]}")
