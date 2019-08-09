import matplotlib.pyplot as plt
from subSeq import subSeq

def plot(genome, window, interval):
    '''Plots each base and their frequency in each area of a genome'''
    bases = list(set(genome))
    if "N" in bases: # Is this condition necessary?
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
	# Need to fix ranges somehow: 0% to 45%?

def get_genome(path): # Again better to use accession number here 
    '''Obtains the genome using a given path'''
    file = open(path,"r")
    genome = file.read()
    file.close()
    return genome # Move this useful file and import it 

def plot_all(genome,windows = [10,100,500]):
    '''Contains window and interval values to plot'''
	for w in windows: plot(genome, w, 1)
	
path = "..\..\data\mtDNA.fa" # Accession number
windows = [10,100,500]
Nshuffle = 3
genome = get_genome(path)

plot_all(genome,windows)
for x in range(Nshuffle):
    path = f"..\..\data\mtDNA_random_{x+1}.fa" # Move this to top of script
    genome = get_genome(path)
    plot_all(genome,windows)
