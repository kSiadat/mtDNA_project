from bs4 import BeautifulSoup as bs
from urllib import request
import wget

path = "../../data/"
fileName = "gene_data_raw.txt"
wget.download("https://www.ncbi.nlm.nih.gov/search/api/sequence/NC_012920", path+"mtDNA.fa")
wget.download("https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?db=nuccore&report=gff3&id=NC_012920.1", path+fileName)
file = open(path+fileName)

text = [line for line in file.readlines()]
print(text)
