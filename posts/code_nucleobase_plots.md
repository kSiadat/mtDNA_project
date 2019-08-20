# Creating the code to draw nucleobase plots
The program talked about here is [plot_mtDNA.py](../code/plot_mtDNA.py) and it can be broken down in to 3 main parts: getting the mitochondrial genome sequence, calculating the proportions of each base, and creating the plots.

## Getting the data
The only data needed for this program is the genome sequence which is stored in the NCBI database and can be accessed using the get_genome function.

This is a very important function and it is used in all of my programs directly or indirectly. It takes the accession number as a parameter, then returns the genome sequence associated with that accession number as a string.

```python
from urllib import request

def get_genome(accession):
    '''Gets text using a url then returns the genome as a string'''
    return "".join(str(get_webData(f"https://www.ncbi.nlm.nih.gov/search/api/sequence/{accession}")).split("\\r\\n")[1:])[:-1]
```

## Calculating nucleobase proportions
This part of the program uses 1 function to do all of the calculations. It looks at all of the bases in the genome, then for each one it counts the number of that base in a given window then divides by the window size. This repeats for every position a long the genome and every base that isn't 'N'. This is because N is recorded when the computer is unsure what to class a base as during the sequencing process.

The function subSeq is used to ensure that any windows that cross over the start or end wrap around again from the other side.
```python
def calc_fractions(genome, window):
    '''Calculates the fractions each base a long a genome'''
    bases = list(set(genome))
    bases.sort()
    return [[subSeq(i,window,genome).count(base)/(2*window + 1) for i in range(len(genome))] for base in bases if base!="N"]
```

## Drawing the plots
For creating the plots I used the python module matplotlib. It it good because it comes with many options about how you want your plot to be drawn. The only issues I had was that the largest relative (scales with the image) font size was not large enough, so I had to use an absolute value.

I also had the problem that I had to save the images manually,but I think that with a bit more time and research that would have been possible.
