from urllib import request
import wget
import os


def replace(link, path):
    if os.path.exists(path):
        os.remove(path)
    wget.download(link, path) # think about urllib here


def extract_sequence(path): # Move to utility script, added argument!
    file = open(f"{path}{file_sequence}", "r")
    lines = [l.rstrip() for l in file.readlines()]
    file.close()
    genome = "".join(lines[1:])
    return genome


def write_sequence(genome, path):
    file = open(f"{path}mtDNA.fa", "w+")
    file.write(genome)
    file.close()


def extract_genes(genome_length, path, accession, desired = ["gene", "rRNA", "tRNA", "D_loop"]):
    file = open(f"{path}{file_gff}", "r")
    text = [line for line in file.readlines()]
    file.close()

    text = [line for line in text if line[:11]==accession]
    text = [line[:-1] for line in text] # use rstrip instead?
    text = [line.split("\t") for line in text]
    text = [line for line in text if line[2] in desired]

    data = [[line[8][line[8].index("-")+1:line[8].index(";")], line[3], line[4], desired.index(line[2]), line[6]] for line in text]
    for d in range(len(text)):
        if text[d][2] == "D_loop":
            data[d][0] = "D-loop"
    data = [data[d] for d in range(len(data)) if data[d][0]!=data[(d+1)%len(data)][0]]

    if int(data[-1][2]) >= genome_length:
        data.append(data[-1][:])
        data[-1][1] = 0
        data[-1][2] = str(int(data[-1][2]) - genome_length)
        data[-2][2] = str(genome_length-1)
    return data


def write_karyotype(data, genome_length, colours = ["dred", "vdgreen", "lblue", "lgrey"]):
    text = f"chr - mt1 MT 0 {genome_length} white\n"
    for d, D in enumerate(data):
        text += f"band mt1 gn{d+1} {D[0]} {D[1]} {D[2]} {colours[D[3]]}\n"
    file = open(f"{path}karyotype.human.mt.txt", "w+") # make that general
    file.write(text)
    file.close()


def write_band_labels(data, genome_length):
    text = ""
    for d, D in enumerate(data):
        if data[d][0] != data[d-1][0]:
            if data[d][0] == data[d+1][0]:
                centre = (int(data[d][1]) + int(data[d+1][2]) + genome_length) // 2
                if centre >= genome_length:
                    centre -= genome_length
                text += f"mt1 {centre} {centre} {D[0]}\n"
            else:
                text += f"mt1 {D[1]} {D[2]} {D[0]}\n"
    file = open(f"{path}karyotype.human.mt.band_labels.txt", "w+") # More general
    file.write(text)
    file.close()


accession = "NC_012920.1"

path = "../../data/"
file_sequence = "{accession}.fa"
file_gff = "gene_data_raw.txt"



replace(f"https://www.ncbi.nlm.nih.gov/search/api/sequence/{accession}", f"{path}{file_sequence}")
replace(f"https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?db=nuccore&report=gff3&id={accession}", f"{path}{file_gff}")

genome = extract_sequence(path)
write_sequence(genome, path)

data = extract_genes(len(genome), path)
write_karyotype(data, len(genome), path)
write_band_labels(data, len(genome), path)
