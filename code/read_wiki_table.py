from bs4 import BeautifulSoup as bs
from urllib import request

path = "https://en.wikipedia.org/wiki/Human_mitochondrial_genetics"

webFile = request.urlopen(path).read()
html = bs(webFile, features = "html.parser")

print(html.table.prettify())
