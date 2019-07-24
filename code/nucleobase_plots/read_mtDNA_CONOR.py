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

# Test the function.
# It's good to have tests in case we ever want to make improvements
# Might be worth looking at this: https://stackoverflow.com/questions/8951020/pythonic-circular-list
assert(subSeq(3,2,"elephant")=="lepha")
assert(subSeq(0,2,"elephant")=="ntele")
assert(subSeq(6,3,"elephant")=="phantel")
assert(subSeq(5,7,"elephant")=="ntelephanteleph")
assert(subSeq(2,10, "elephant")=="elephantelephanteleph")

path="..\data\mtDNA.fa"

file = open(path,"r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

genome = "".join(lines[1:])

bases = list(set(genome))
bases.sort()
print(bases)

counts = {b:genome.count(b) for b in bases}
print(counts)

window = 10
fractions = {base:[subSeq(i,window,genome).count(base)/(2*window + 1) for i in range(0,len(genome))] for base in bases}

for base in bases: print(base); print(fractions[base][0:10])



    





