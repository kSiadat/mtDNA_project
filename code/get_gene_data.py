from mtdna_utilities import get_genome, get_gff, get_webData, write_file
import os
from urllib import request


def extract_genes(accession, text, genomeLength, desired = ["gene", "rRNA", "tRNA", "D_loop"]):
    '''Extracts the gene data from gff format'''
    text = str(text).split("\\n")
    text = [line for line in text if line[:11]==accession]
    text = [line.split("\\t") for line in text]
    text = [line for line in text if line[2] in desired]

    data = [[line[8][line[8].index("-")+1:line[8].index(";")], line[3], line[4], desired.index(line[2]), line[6]] for line in text]
    for d in range(len(text)):
        if text[d][2] == "D_loop":
            data[d][0] = "D-loop"
    data = [data[d] for d in range(len(data)) if data[d][0]!=data[(d+1)%len(data)][0]]

    if int(data[-1][2]) >= genomeLength:
        data.append(data[-1][:])
        data[-1][1] = 0
        data[-1][2] = str(int(data[-1][2]) - genomeLength + 1)
        data[-2][2] = str(genomeLength-1)
    return data


def write_karyotype(accession, path, data, genomeLength,  colours = ["dred", "vdgreen", "lblue", "lgrey"]):
    '''Creates a karyotype file for circos'''
    strandOuter = f"chr - mt1 MT 0 {genomeLength-1} white\n"
    strandInner = ""
    last = int(data[0][1])
    for d, D in enumerate(data):
        if D[4] == "+":
            strandOuter += f"band mt1 gn{d+1} {D[0]} {D[1]} {D[2]} {colours[D[3]]}\n"
        else:
            if int(D[1]) > last+1:
                strandInner += f"mt1 {last+1} {int(D[1])-1} color=white\n"
            strandInner += f"mt1 {D[1]} {D[2]} color={colours[D[3]]}\n"
            last = int(D[2])
    if int(data[-1][1])==0 and data[-1][4]=="-" and int(data[0][1])>int(data[-1][2])+1:
        strandInner += f"mt1 {data[-1][2]+1} {data[0][1]-1} color=white\n"
    write_file(f"{path}karyotype.{accession}.+.txt", strandOuter)
    write_file(f"{path}karyotype.{accession}.-.txt", strandInner)


def write_band_labels(accession, path, data, genomeLength):
    '''Creates a file that allows circos to draw gene labels'''
    text = ""
    for d, D in enumerate(data):
        if data[d][0] != data[d-1][0]:
            if data[d][0] == data[(d+1)%len(data)][0]:
                centre = (int(data[d][1]) + int(data[d+1][2]) + genomeLength) // 2
                if centre >= genomeLength:
                    centre -= genomeLength
                text += f"mt1 {centre} {centre} {D[0]}\n"
            else:
                text += f"mt1 {D[1]} {D[2]} {D[0]}\n"
    write_file(f"{path}karyotype.{accession}.band_labels.txt", text)


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
    accession = "NC_012920.1"
    path = "../data/"
    get_gene_data(accession, path)
