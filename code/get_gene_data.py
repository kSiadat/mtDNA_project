from mtdna_utilities import get_genome, get_gff, get_webData, write_file
import os
from urllib import request


def extract_genes(accession, text, genomeLength, desired = ["gene", "rRNA", "tRNA", "D_loop"]):
    '''Extracts the gene data from gff format'''
    text = str(text).split("\\n")
    text = [line for line in text if line[:11]==accession]
    text = [line.split("\\t") for line in text]
    text = [line for line in text if line[2] in desired]

    data = [["", line[3], line[4], desired.index(line[2]), line[6]] for line in text]
    for d in range(len(data)):
        for t in range(len(text[d][8])):
            if text[d][8][t:t+6] == ";Name=":
                data[d][0] = text[d][8][t+6:t+6+text[d][8][t+6:].index(";")]
    for d in range(len(text)):
        if text[d][2] == "D_loop":
            data[d][0] = "D-loop"
    for d in range(len(data)):
        if data[d-1][1]==data[d][1] and data[d-1][2]==data[d][2]:
            data[d][0] = data[d-1][0]

    data = [data[d] for d in range(len(data)) if data[d][0]!=data[(d+1)%len(data)][0]]
    data = [data[d] for d in range(len(data)) if data[d][0]!=""]

    if int(data[-1][2]) >= genomeLength:
        data.append(data[-1][:])
        data[-1][1] = 0
        data[-1][2] = str(int(data[-1][2]) - genomeLength + 1)
        data[-2][2] = str(genomeLength-1)
    for D in data:
        print(D)
    return data


def write_karyotype(accession, path, data, genomeLength,  colours = ["dred", "vdgreen", "lblue", "lgrey"]):
    '''Creates a karyotype file for circos'''
    end = -1
    while data[end][4] != "-":
        end -= 1
    start = 0
    while data[start][4] != "-":
        start+=1
    strandOuter = f"chr - mt1 MT 0 {genomeLength-1} white\n"
    strandInner = ""
    last = 0
    for d, D in enumerate(data):
        if D[4] == "+":
            strandOuter += f"band mt1 gn{d+1} {D[0]} {D[1]} {D[2]} {colours[D[3]]}\n"
        else:
            if int(D[1]) > last+1:
                strandInner += f"mt1 {last+1} {int(D[1])-1} color=white\n"
            strandInner += f"mt1 {D[1]} {D[2]} color={colours[D[3]]}\n"
            last = int(D[2])
    if int(data[-1][1])==0 and data[-1][4]=="-" and int(data[start][1])>int(data[-1][2])+1:
        strandInner += f"mt1 {int(data[-1][2])+1} {int(data[start][1])-1} color=white\n"
    if int(data[end][1])>0 and int(data[end][2])<genomeLength-1:
        strandInner += f"mt1 {int(data[end][2])+1} {genomeLength-1} color=white\n"
    write_file(f"{path}karyotype.{accession}.+.txt", strandOuter)
    write_file(f"{path}karyotype.{accession}.-.txt", strandInner)


def write_band_labels(accession, path, data, genomeLength):
    '''Creates a file that allows circos to draw gene labels'''
    strandOuter = ""
    strandInner = ""
    for d, D in enumerate(data):
        if data[d][0] != data[d-1][0]:
            if data[d][0] == data[(d+1)%len(data)][0]:
                centre = (int(data[d][1]) + int(data[d+1][2]) + genomeLength) // 2
                if centre >= genomeLength:
                    centre -= genomeLength
                if D[4] == "+":
                    strandOuter += f"mt1 {centre} {centre} {D[0]}\n"
                else:
                    strandInner += f"mt1 {centre} {centre} {D[0]}\n"
            else:
                if D[4] == "+":
                    strandOuter += f"mt1 {D[1]} {D[2]} {D[0]}\n"
                else:
                    strandInner += f"mt1 {D[1]} {D[2]} {D[0]}\n"
    write_file(f"{path}karyotype.{accession}.+.band_labels.txt", strandOuter)
    write_file(f"{path}karyotype.{accession}.-.band_labels.txt", strandInner)


def get_gene_data(accession, path):
    genomeLength = len(get_genome(accession))
    text = get_gff(accession)

    data = extract_genes(accession, text, genomeLength)
    print("Extracted gene data")
    write_karyotype(accession, path, data, genomeLength)
    print("Created karyotype file")
    write_band_labels(accession, path, data, genomeLength)
    print("Created gene label file\n")


if __name__ == "__main__":
    accession = "NC_001224.1"
    path = "../data/temp/"
    get_gene_data(accession, path)
