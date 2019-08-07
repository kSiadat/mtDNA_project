from bs4 import BeautifulSoup as bs
from urllib import request
import wget


def download(path, fileName):
    wget.download("https://www.ncbi.nlm.nih.gov/search/api/sequence/NC_012920", path+"mtDNA.fa")
    wget.download("https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?db=nuccore&report=gff3&id=NC_012920.1", path+fileName)


def extract(path, fileName):
    file = open(path+fileName)
    text = [line for line in file.readlines()]
    file.close()

    text = [line for line in text if line[:11]=="NC_012920.1"]
    text = [line[:-1] for line in text]
    text = [line.split("\t") for line in text]
    text = [line for line in text if line[2] in desired]

    data = [[line[8][line[8].index("-")+1:line[8].index(";")], line[3], line[4], desired.index(line[2]), line[6]] for line in text]
    for d in range(len(text)):
        if text[d][2] == "D_loop":
            data[d][0] = "D_loop"
    data = [data[d] for d in range(len(data)) if data[d][0]!=data[(d+1)%len(data)][0]]
    return data


def karyotype(path, data):
    text = "chr - mt1 MT 0 " + data[-1][2] + " white\n"
    for d, D in enumerate(data):
        text += "band mt1 gn" + str(d+1) + " " + D[0] + " " + D[1] + " " + D[2] + " " + colours[D[3]] + "\n"
    file = open(path+"karyotype.human.mt.txt", "w+")
    file.write(text)
    file.close()


def band_labels(path, data):
    text = ""
    for d, D in enumerate(data):
        text += "mt1" + " " + D[1] + " " + D[2] + " " + D[0] + "\n"
    file = open(path+"karyotype.human.mt.band_labels.txt", "w+")
    file.write(text)
    file.close()


path = "../../data/"
fileName = "gene_data_raw.txt"
desired = ["gene", "rRNA", "tRNA", "D_loop"]
colours = ["dred", "vdgreen", "lblue", "lgrey"]

try:
    data = extract(path, fileName)
except FileNotFoundError:
    download(path, fileName)
    data = extract(path, fileName)
karyotype(path, data)
band_labels(path, data)
