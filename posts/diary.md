# Diary

### 2019-07-15
* Created mtDNA_project repository on github
* Researched about mtDNA and started writing an article about it
* Installed circos **Link to website - CONOR**
* Edited system path to add circos to it

### 2019-07-16
* Added suggested changes to the article and repository
* Installed Github desktop
* Created research diary
* Thought about extraxting information from websites with beautiful soup 4
* Created python program to parse mtDNA genome, and calculate the proportion of each base in a given range **Link to code - CONOR**
* Updated the repository structure

### 2019-07-18
* Added suggested changes to the article and repository
	* Changed URLs to DOIs where possible **Link to description of DOIs - CONOR**
	* Changed reference links to be more scientific/ more natural
* Created system path to python to allow installation of beautifulsoup and matplotlib **Link to package pages - CONOR**
* Checked and understood Conor's code **Link to code - CONOR**
* Looked up list comperhension and a few of python's inbuilt methods
* Looked up how to use matplotlib
* Used matplotlib to create a function to plot fraction of bases, given a sampling rate and a sample window size
* Created randomly generated genome, and plotted it in the same way as the actual genome **Say why - CONOR**
**Mention choice of window size - CONOR**

###2019-07-19
* Added axis labels and removed N from the mitochondrial genome graphs
* Wrote a post about the mitochondrial genome graphs **Add plots to the post - CONOR**
* Learnt how to use beautiful soup 4

Comment out markdown code: https://stackoverflow.com/questions/4823468/comments-in-markdown

Download HTML as string: https://stackoverflow.com/questions/16025368/download-file-as-string-in-python
from urllib.request import urlopen
~~~~
data = urlopen('http://www.google.com').read() #bytes
body = data.decode('utf-8')
~~~~

Why is there N in mtDNA sequence:
https://biology.stackexchange.com/questions/1830/why-are-there-ns-after-sanger-sequencing
Where does this sequence come from?

mtDNA review: https://doi.org/10.1016/j.bbabio.2009.09.005

Want to be able to progamatically generate better versions of plots like Figure 3 from this paper:
http://embomolmed.embopress.org/content/6/2/183

Want to be able to programatically generate better versions of plots like this one on wikipedia:
https://upload.wikimedia.org/wikipedia/commons/1/15/Map_of_the_human_mitochondrial_genome.svg
