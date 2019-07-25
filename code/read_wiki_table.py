from bs4 import BeautifulSoup as bs
from urllib import request

def breakdown_table1(table):
    def extract_name(link):
        link = link[:-4]
        for c in range(len(link)):
            if link[len(link)-c-1] == ">":
                return link[len(link)-c:]

    def extract_range(nums):
        if "(" in nums:
            nums = nums[nums.index("("):]
        nums = nums.replace(",", "")
        print(nums.index("-"))
        print(type(nums), nums, nums.split("-"))
        return nums.split("-")

    data = table.find_all("td")
    output = []
    for d in range(len(data)):
        data[d] = str(data[d])[4:-6]
    for d in range(len(data)):
        if data[d][:2] == "<a":
            gene = extract_name(data[d])
            print(gene)
            nums = extract_range(data[d+1])
            print(nums)
            start = nums[0]
            end = nums[1]
            strand = data[d+2]
            output.append([gene, start, end, strand])
    return output

path = "https://en.wikipedia.org/wiki/Human_mitochondrial_genetics"

webFile = request.urlopen(path).read()
html = bs(webFile, features = "html.parser")

table1 = html.find_all("table")[1]
genes1 = breakdown_table1(table1)
for G in genes1:
    print(G)
