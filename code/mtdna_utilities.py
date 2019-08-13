import os
import random
from bs4 import BeautifulSoup as bs
from urllib import request


def subSeq(centre, window, seq):
    '''Get a windowed subset of a circular string/sequence'''
    start = centre - window
    end = centre + window
    if start >= 0 and end < len(seq):
        subseq = seq[start:(end+1)]
    elif start < 0 and end >= len(seq):
        subseq = seq[start:]+seq+seq[0:(end-len(seq)+1)]
    elif start < 0:
        subseq = seq[start:]+seq[0:(end+1)]
    elif end >= len(seq):
        subseq = seq[start:]+seq[0:(end-len(seq)+1)]
    return(subseq)

def write_file(path, text):
    '''Takes a path including filename and writes text to that file'''
    file = open(path, "w+")
    file.write(text)
    file.close()

def delete(path):
    if os.path.exists(path):
        os.remove(path)

def download(path, url):
    '''Deletes the file if it exists, then downloads it'''
    delete(path)
    wget.download(path, url)

def get_webData(url, html=False):
    '''Gets the text from a url'''
    text = request.urlopen(url).read()
    if html:
        return bs(text, features="html.parser")
    return text

def get_genome(accession):
    '''Gets text using a url then returns the genome as a string'''
    return "".join(str(get_webData(f"https://www.ncbi.nlm.nih.gov/search/api/sequence/{accession}")).split("\\r\\n")[1:])[:-1]

def get_gff(accession):
    '''Gets a raw gff file in text'''
    return get_webData(f"https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?db=nuccore&report=gff3&id={accession}")

def generate_genome(genome):
    '''Reshuffles an existing genome in to a random order'''
    genome = list(genome)
    random.shuffle(genome)
    return "".join(genome)

def calc_fractions(genome, window):
    '''Calculates the fractions each base a long a genome'''
    bases = list(set(genome))
    bases.sort()
    return [[subSeq(i,window,genome).count(base)/(2*window + 1) for i in range(len(genome))] for base in bases if base!="N"]
