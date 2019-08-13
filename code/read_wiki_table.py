from mtdna_utilities import get_webData
from bs4 import BeautifulSoup as bs
from urllib import request


def breakdown_table(table):
    '''Returns the data required from the wiki tables'''
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


url = "https://en.wikipedia.org/wiki/Human_mitochondrial_genetics"
html = get_webData(url, html=True)

genes = []
for t in range(3):
    table = html.find_all("table")[t+1]
    genes += breakdown_table(table)

