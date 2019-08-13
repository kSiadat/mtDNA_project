from mtdna_utilities import calc_fractions, generate_genome, get_genome, subSeq
import matplotlib.pyplot as plt


def plot(window, fractions, bases, yRange):
    print(yRange)
    '''Plots each base and their frequency in each area of a genome'''
    for b in range(len(bases)):
        plt.plot([f for f in range(len(fractions[b]))], [fractions[b][f] for f in range(len(fractions[b]))])
    plt.legend(bases, fontsize=30, loc="upper right")
    plt.xlabel("Genome coordinate", fontsize=30)
    plt.ylabel("Proportion of base", fontsize=30)
    plt.tick_params(axis='both', which='major', labelsize=20)
    plt.ylim(0, yRange)
    plt.show()


def find_max(genomes, windows):
    '''Returns all of the fractions and maximum values for each window'''
    fractions = [[calc_fractions(G, W) for G in genomes] for W in windows]
    maxValues = [[[max(B) for B in fractions[w][g]] for g in range(len(fractions[w]))] for w in range(len(fractions))]
    maxValues = [[max(G) for G in maxValues[w]] for w in range(len(maxValues))]
    maxValues = [max(W) for W in maxValues]
    return fractions, maxValues


accession = "NC_012920.1"
windows = [10, 100, 500]
numShuffles = 3
bases = ["A", "C", "T", "G"]

genomes = [get_genome(accession)]
for x in range(numShuffles):
    genomes.append(generate_genome(genomes[0]))

fractions, maxValues = find_max(genomes, windows)
for w, W in enumerate(windows):
    for g in range(len(genomes)):
        plot(W, fractions[w][g], bases, maxValues[w])
