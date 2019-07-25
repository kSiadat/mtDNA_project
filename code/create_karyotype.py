from bs4 import BeautifulSoup as bs
from urllib import request

def breakdown_table(table):
    def extract_name(link):
        link = link[:-4]
        for c in range(len(link)):
            if link[len(link)-c-1] == ">":
                return link[len(link)-c:]

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
                output.append([gene, start, end, strand])
    return output

def create_karyotype(data):
    text = ""
    for d in range(len(data)):
        if d != 0 and d%22 == 0:
            colour = "x"
        elif d != 0 and d%23 == 0:
            colour = "y"
        else:
            colour = d+1
            while colour > 23:
                colour -=24
            colour = str(colour)
        text += "chr - mt" + str(d+1) + " " + data[d][0] + " " + data[d][1] + " " + data[d][2] + " chr" + colour +"\n"
    file = open("../data/karyotype.mt.txt", "w+")
    file.write(text)
    file.close()

path = "https://en.wikipedia.org/wiki/Human_mitochondrial_genetics"

webFile = request.urlopen(path).read()
html = bs(webFile, features = "html.parser")

data = []
for t in range(3):
    table = html.find_all("table")[t+1]
    data += breakdown_table(table)

create_karyotype(data)
