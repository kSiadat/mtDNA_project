import matplotlib.pyplot as plt
from subSeq import subSeq

def plot(genome, window, interval):
    '''Plots a graph of each base and their frequency in each area of a genome'''
    bases = list(set(genome))
    if "N" in bases:
        del bases[bases.index("N")]
    bases.sort()

    fractions = [[subSeq(i*interval,window,genome).count(base)/(2*window + 1) for i in range((len(genome)//interval)+1)] for base in bases]

    for b in range(len(bases)):
        plt.plot([f*interval for f in range(len(fractions[b]))], [fractions[b][f] for f in range(len(fractions[b]))])
    plt.axvline(x=0, color="k")
    plt.axvline(x=len(genome)-1, color="k")
    plt.legend(bases, fontsize=30, loc="upper right")
    plt.xlabel("Genome coordinate", fontsize=30)
    plt.ylabel("Proportion of base", fontsize=30)
    plt.tick_params(axis='both', which='major', labelsize=20)
    plt.show()

def get_genome(path):
    '''Obtains the genome using a given path'''
    file = open(path,"r")
    lines = [l.rstrip() for l in file.readlines()]
    file.close()
    return "".join(lines[1:])

def plot_all(genome):
    '''Contains window and interval values to plot'''
    #plot(genome, 10, 1)
    #plot(genome, 100, 1)
    plot(genome, 500, 1)

path = "..\..\data\mtDNA.fa"
genome = get_genome(path)
plot_all(genome)
for x in range(3):
    path = f"..\..\data\mtDNA_random_{x+1}.fa"
    genome = get_genome(path)
    plot_all(genome)
