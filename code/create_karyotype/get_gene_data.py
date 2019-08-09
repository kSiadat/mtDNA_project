from bs4 import BeautifulSoup as bs
from urllib import request
import wget
import os


def replace(link, path):
    if os.path.exists(path):
        os.remove(path)
    wget.download(link, path)


def extract():
    file = open(f"{path}{file_gff}")
    text = [line for line in file.readlines()]
    file.close()

    text = [line for line in text if line[:11]=="NC_012920.1"]
    text = [line[:-1] for line in text]
    text = [line.split("\t") for line in text]
    text = [line for line in text if line[2] in desired]

    data = [[line[8][line[8].index("-")+1:line[8].index(";")], line[3], line[4], desired.index(line[2]), line[6]] for line in text]
    for d in range(len(text)):
        if text[d][2] == "D_loop":
            data[d][0] = "D-loop"
    data = [data[d] for d in range(len(data)) if data[d][0]!=data[(d+1)%len(data)][0]]
    return data


def karyotype(data):
    text = f"chr - mt1 MT 0 {data[-1][2]} white\n"
    for d, D in enumerate(data):
        text += f"band mt1 gn{d+1} {D[0]} {D[1]} {D[2]} {colours[D[3]]}\n"
    file = open(f"{path}karyotype.human.mt.txt", "w+")
    file.write(text)
    file.close()


def band_labels(data):
    text = ""
    for d, D in enumerate(data):
        text += f"mt1 {D[1]} {D[2]} {D[0]}\n"
    file = open(f"{path}karyotype.human.mt.band_labels.txt", "w+")
    file.write(text)
    file.close()


path = "../../data/"
file_sequence = "mtDNA.fa"
file_gff = "gene_data_raw.txt"
desired = ["gene", "rRNA", "tRNA", "D_loop"]
colours = ["dred", "vdgreen", "lblue", "lgrey"]

replace("https://www.ncbi.nlm.nih.gov/search/api/sequence/NC_012920.1", f"{path}{file_sequence}")
replace("https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?db=nuccore&report=gff3&id=NC_012920.1", f"{path}{file_gff}")
data = extract()
karyotype(data)
band_labels(data)
