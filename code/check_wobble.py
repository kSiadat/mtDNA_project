from mtdna_utilities import get_genome
from read_wiki_table import *

gnome = get_genome("NC_012920.1")
glist = {g[0]:[int(g[1]),int(g[2]),g[3]] for g in genes}
gorder = [g[0] for g in genes]

for g in gorder:
    print(g)
    gene = gnome[(glist[g][0]-1):(glist[g][1])]
    print(gene[0:30])
