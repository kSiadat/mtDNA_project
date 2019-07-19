import matplotlib.pyplot as plt

def subSeq(centre,window,seq):
    '''Get a windowed subset of a circular string/sequence'''
    start = centre - window
    end = centre + window
    if start >= 0 and end < len(seq):
        subseq = seq[start:(end+1)]
    elif start < 0 and end >= len(seq):
        subseq = seq[start:]+seq+seq[0:(end-len(seq)+1)]
    elif start < 0:
        subseq = seq[start:]+seq[0:(end+1)]
    elif end >= len(seq):
        subseq = seq[start:]+seq[0:(end-len(seq)+1)]
    return(subseq)

def plot(genome, window, interval):
    #Plots a graph of each base and their frequency in each area of a genome
    bases = list(set(genome))
    bases.sort()

    fractions = [[subSeq(i*interval,window,genome).count(base)/(2*window + 1) for i in range((len(genome)//interval)+1)] for base in bases]

    for b in range(len(bases)):
        plt.plot([f*interval for f in range(len(fractions[b]))], [fractions[b][f] for f in range(len(fractions[b]))])
    plt.axvline(x=0, color="k")
    plt.axvline(x=len(genome)-1, color="k")
    plt.legend(bases)
    plt.show()


# Test the function.
# It's good to have tests in case we ever want to make improvements
# Might be worth looking at this: https://stackoverflow.com/questions/8951020/pythonic-circular-list
assert(subSeq(3,2,"elephant")=="lepha")
assert(subSeq(0,2,"elephant")=="ntele")
assert(subSeq(6,3,"elephant")=="phantel")
assert(subSeq(5,7,"elephant")=="ntelephanteleph")
assert(subSeq(2,10, "elephant")=="elephantelephanteleph")

path1="..\data\mtDNA.fa"
path2="..\data\mtDNA_random.fa"


file = open(path1,"r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

genome = "".join(lines[1:])

"""
bases = list(set(genome))
bases.sort()
print(bases)

counts = {b:genome.count(b) for b in bases}
print(counts)

window = 10
fractions = {base:[subSeq(i,window,genome).count(base)/(2*window + 1) for i in range(0,len(genome))] for base in bases}

for base in bases: print(base); print(fractions[base][0:10])
"""
plot(genome, 10, 1)
#plot(genome, 20, 2)
plot(genome, 50, 10)
plot(genome, 100, 50)
plot(genome, 500, 10)
plot(genome, 1000, 1)

