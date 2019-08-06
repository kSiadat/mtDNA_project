from bs4 import BeautifulSoup as bs
from urllib import request

def breakdown_table(table, order):
    def extract_name(link):
        link = link[:-4]
        for c in range(len(link)):
            if link[len(link)-c-1] == ">":
                return link[len(link)+3-c:]

    def extract_range(nums):
        if "(" in nums:
            nums = nums[:nums.index("(")]
        nums = nums.replace(",", "")
        for c in range(len(nums)):
            if not nums[c].isdigit():
                return nums[:c], nums[c+1:]

    data = table.find_all("td")
    output = []
    for d in range(len(data)):
        data[d] = str(data[d])[4:-6]
    for d in range(len(data)):
        if data[d][:2] == "<a":
            gene = extract_name(data[d])
            nums = extract_range(data[d+1])
            start = nums[0]
            end = nums[1]
            strand = data[d+2]
            if start != "":
                output.append([gene, int(start), end, order, strand])
    return output

def create_karyotype(data):
    colours = ["dred", "vdgreen", "lblue"]
    text = "chr - mt1 MT 0 " + data[-1][2] + " white\n"
    for d in range(len(data)):
        text += "band mt1 gn" + (str(d+1)) + " " + data[d][0] + " " + data[d][1] + " " + data[d][2] + " " + colours[data[d][3]] + "\n"
    file = open("../../data/karyotype.mt.colour_by_table.txt", "w+")
    file.write(text)
    file.close()

def create_karyotype_label(data):
    text = ""
    for d in range(len(data)):
        text += "mt1" + " " + data[d][1] + " " + data[d][2] + " " + data[d][0] + "\n"
    file = open("../../data/karyotype.mt.band_labels.txt", "w+")
    file.write(text)
    file.close()

url = "https://en.wikipedia.org/wiki/Human_mitochondrial_genetics"

webFile = request.urlopen(url).read()
html = bs(webFile, features = "html.parser")

data = []
for t in range(3):
    table = html.find_all("table")[t+1]
    data += breakdown_table(table, t)
data.sort(key = lambda x: x[1])
for d in range(len(data)):
    data[d][1] = str(data[d][1])

create_karyotype(data)
create_karyotype_label(data)
