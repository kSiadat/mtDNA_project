from bs4 import BeautifulSoup as bs
import urllib

path = "https://en.wikipedia.org/wiki/Mitochondrial_DNA"

response = urllib.urlopen('http://python.org/')
html = response.read()
html = bs(file)
