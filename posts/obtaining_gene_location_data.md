# Obtaining data on the location of genes in human mtDNA

## Why do I want the data?
In order to create a circos image of the mitochondrial genome, circos needs a [karyotype](https://en.wikipedia.org/wiki/Karyotype) file. A karyotype file is a text file that contains information about the name, size, location, and colour of all of the chromosomes in a genome. It also has bands which are sections within chromosomes, which I use to represent genes.

Circos didn't come with a karytotype file for mitochondria, and I didn't already have the information about the mitochondrial genome that would allow me to create a karyotype file. So I had to get it from somewhere.

## From the wikipedia page
The first place that I tried to get information from was the wikipedia page on human mitochondrial genetics, which contains 3 tables about the location of each of the genes in the mitochondrial genome, as well as their name and strand (mitochondrial genomes have 2 seperate strands, the light and heavy).

To do this I used the python modules urllib (which allows you to access webpages using a URL) and BeautifulSoup4 (bs4) (which allows you to easily parse html). Once I had read the webpage with urllib I used bs4 to zoom in on sections I wanted, then to break it down in to a format that I could extract the data from.

This works fine for that wiki page, however if I wanted to get the same information for a different species (e.g. yeast), I would have to parse a different wiki page and the tables it contains. Those tables would probably have a different format and so I woudl have to write a whole new program.

## From the UCSC table browser
The UCSC table browser is a way to access a database that contains the information I want and a lot more as well. It also stores all of the data in a standardised format which means I would only need 1 program to read all the data I need from it.

The problem is that it is quite hard to use as it contains a lot of technical biology terms and even the help guide doesn't entirley make sense to me.