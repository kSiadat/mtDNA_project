# Obtaining data on the location of genes in human mtDNA

## Why do I want the data?
In order to create a circos image of the mitochondrial genome, circos needs a [karyotype](https://en.wikipedia.org/wiki/Karyotype) file. A karyotype file is a text file that contains information about the name, size, location, and colour of all of the chromosomes in a genome. It also has bands which are sections within chromosomes, which I use to represent genes.

Circos didn't come with a karytotype file for mitochondria, and I didn't already have the information about the mitochondrial genome that would allow me to create a karyotype file. So I had to get it from somewhere.

## From the wikipedia page
The first place that I tried to get information from was the wikipedia page on [human mitochondrial genetics](https://en.wikipedia.org/wiki/Human_mitochondrial_genetics), which contains 3 tables about the location of each of the genes in the mitochondrial genome, as well as their name and [strand](https://en.wikipedia.org/wiki/Mitochondrial_DNA#Genes_on_the_mtDNA_and_their_transcription).

I used python to read the tables on the webpage. This approach works fine for that wiki page, however if I wanted to get the same information for a different species (e.g. yeast), I would have to parse a different wiki page and the tables it contains. Those tables would probably have a different format and so I would have to write a whole new program.

As I can also use the NCBI for the same purpose, which is more stable and reliable, I have stopped using the wiki page to get this data. However the NCBI database does not have the respiratory complex of each gene, so in order to get that information I will have to use the wiki page.

## From the UCSC table browser
The [UCSC table browser](http://genome.ucsc.edu/cgi-bin/hgTables) is a way to access a database that contains the information I want and a lot more as well. It also stores all of the data in a standardised format which means I would only need 1 program to read all the data I need from it.

The problem is that it is quite hard to use as it contains a lot of technical biology terms and even the help guide doesn't entirley make sense to me. It is also harder to do programmatically, so I have chosen not to use this option.

## From the NCBI database
The [NCBI](https://www.ncbi.nlm.nih.gov/) (National Centre for Biotechnology Information) has lots of data stored about many different kinds of genome. They have a complete mtDNA sequence as well as a [.gff](https://en.wikipedia.org/wiki/General_feature_format) file.

I was able to access these files using python, and they are very easy to use because they are stored in a standardised format. It is important to note, that because the NCBI database is well structured, I have made it so that in order to access the same files for a different species, you just have to get the accession number and give that to the program.
