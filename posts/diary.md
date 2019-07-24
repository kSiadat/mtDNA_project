# Diary

### 2019-07-15
+ Created mtDNA_project repository on github
+ Researched about mtDNA and started writing an article about it, used multiple source although I mostly used 1: [mtDNA review](https://doi.org/10.1016/j.bbabio.2009.09.005).
+ Installed [circos](circos.ca)
+ Edited system path to add circos to it

### 2019-07-16
+ Added suggested changes to the article and repository
+ Installed Github desktop
+ Created research diary
+ Thought about extraxting information from websites with beautiful soup 4
+ Created [python program](code/read_mtDNA.py) to parse mtDNA genome, and calculate the proportion of each base in a given range

### 2019-07-18
+ Added suggested changes to the article and repository
	+ Changed URLs to [DOIs](https://en.wikipedia.org/wiki/Digital_object_identifier) where possible
	+ Changed reference links to be more scientific or more natural, depending on what was being linked too
	+ I wanted to comment out the links so that I could still access them when editing but they wouldn't be visible when viewing the document normally. I found out how to comment [here](https://stackoverflow.com/questions/4823468/comments-in-markdown).
+ Created system path to python to allow installation of [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [matplotlib](https://matplotlib.org/)
+ Checked and understood [Conor's code](code/read_mtDNA_CONOR.py)
+ Looked up [list comperhension](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python) and a few of python's inbuilt methods
+ Looked up how to use [matplotlib](https://matplotlib.org/)
+ Used matplotlib to create a function to plot fraction of bases, given a sampling rate and a sample window size. Different window sizes were experimented with in order to see what size gave the most information in the graph.
+ Created randomly generated genome, and plotted it in the same way as the actual genome. This was to see if there was any difference between the actual and random genome, so that I could know whether the results from the actual genome were significant or not.

### 2019-07-19
+ Added axis labels and removed N from the mitochondrial genome graphs, it turns out [Ns](https://biology.stackexchange.com/questions/1830/why-are-there-ns-after-sanger-sequencing) are entered in to the genome sequence when the computer is unable to clearly identify a base as 1 or another.
+ Wrote a post about the mitochondrial genome graphs
+ Learnt how to use beautiful soup 4, I had a problem with accessing the html from the internet, but found an [answer](https://stackoverflow.com/questions/16025368/download-file-as-string-in-python) at stack overflow, which uses a standard python 3 module called urllib.

### 2019-07-21
+ Added suggestedchanges to do with referencing; added more references to resources used and where to get more information about terms/topics mentioned
+ Added graphs to the post about base graphs, and added some extra comparison details

### 2019-07-22
Today I started with circos. Circos runs using perl, so the 1st thing I had to was install Stawberry Perl, a version of perl available for use on windows sytems. There are also a lot of modules required for circos to run, so I used the command 'circos -modules' to check I had them all, which I did.

Then I started with the tutorials. It actually took me a while to work out that I was writing the configuration file for circos to create the drawing with, but once I figured that out I could run the programs. The 1st tutorial worked fine, but I had a problem with the 2nd tutorial where circos would say there wasn't enough memory.

The aim right now is to be able to prgrammatically generate better versiens of plots such as these: [plot1](http://embomolmed.embopress.org/content/6/2/183), [plot2](https://upload.wikimedia.org/wikipedia/commons/1/15/Map_of_the_human_mitochondrial_genome.svg)

### 2019-07-24
It turns out that I should have had the program split up in to multiple configuration files and 'include' them (basically import them). Although the actual problem that was causing the error must have been me copying down the code from the tutorial wrong, because when running copy pasted code it worked fine. I also uninstalled strawberry perl 23-bit and installed 64-bit since my computer is 64-bit.

Added more references to the diary, that had been sitting around commented out for a while

Resized the labels on the diagrams to make them easier to read. I just guessed that size would be a parameter, but had to look up about [resizing](https://gist.github.com/CnrLwlss/9587f615a7440113430c), and turns out I should use 'fontsize' or 'label_size' instead of just 'size'. I also had to look up how to position the [legend](https://matplotlib.org/3.1.1/api/legend_api.html).

Ran into a problem with not having the data used in 1 of the tutorials, then realised I have already downloaded the tutorials from circos, which come with the necessary data.

Completed going through Quick start tutorial section.