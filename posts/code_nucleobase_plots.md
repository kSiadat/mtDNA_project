# Creating the code to draw nucleobase plots
The program talked about here is [plot_mtDNA.py](../code/plot_mtDNA.py) and it can be broken down in to 3 main parts: getting the mitochondrial genome sequence, calculating the proportions of each base, and creating the plots.

## Getting the data
The only data needed for this program is the genome sequence which is stored in the NCBI database and can be accessed using the get_genome function.

This is a very important function and it is used in all of my programs directly or indirectly. It takes the accession number as a parameter, then returns the genome sequence associated with that accession number as a string.

```python
from urllib import request

def get_genome(accession):
    return "".join(str(get_webData(f"https://www.ncbi.nlm.nih.gov/search/api/sequence/{accession}")).split("\\r\\n")[1:])[:-1]
```
