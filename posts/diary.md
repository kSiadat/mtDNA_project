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

### 2019-07-25
Today I have been parsing the [human mitochondrial genetics](https://en.wikipedia.org/wiki/Human_mitochondrial_genetics) wiki page using [beautiful soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to help me. It has been ok until now, where I have run into a problem; python is unable to use .split("-") properly, [this page](https://stackoverflow.com/questions/33307690/python-ascii-codec-cant-encode-en-dash) suggests that it could be because the text was originally in unicode and python was unable to convert a unicode '-' to an ASCII '-'. Got round this by using .isdigit() to find the index position of the dash character.

I have now finished parsing the [wiki page](https://en.wikipedia.org/wiki/Human_mitochondrial_genetics), and I needed to look up [list concatenation](https://blog.usejournal.com/concatenating-two-lists-in-python-3cf9051da17f). But I still have to create a karyotype file for circos using the data.

Have now created a mitochondrial genome karyotype file for circos, with help from the [circos tutorial](http://circos.ca/documentation/tutorials/ideograms/karyotypes/) on karyotype file structure.

Tested the first tutorial using the mitochondrial karytype file I created and it worked. Tested the 2nd to see the labels but there is an issue, some of the genes seem to have multiple labels which are illegible because they have been placed in the same place. The labels only loked like they were in the same place, actually the genes were so small that the labels were wider than them and so overlapped, I have fixed this but now there is a new problem where the labels extend off the edge of the image.

### 2019-07-26
Removed the MT- from the gene labels in the karyotype file since they just mean mitochondrial gene which you should know anyway if you are looking at the plots.

Fixed the sorting of the karyotype file by putting the sort statement outside of the breakdown_table function so that the whole set of genes would be sorted, instead of having 3 subsets of sorted genes.

Changed the karyotype file and ideogram configuration file so that there is 1 chromosome with multiple bands instead of multiple chromosomes, since 1 loop of mtDNA is 1 chromosome. Changed the chromosome colour to white so it is more seperate from the gene colours, also made the ideogram thicker.

Wrote about obtaining the information needed to write a karyotype file, and so create a circos image of the human mitochondrial genome.

Created data files for circos to use to create line plots for nucleobase proportions. Plotted nucleobase line plots on to circos image, tried to add axes to them but couldn't get them to position correctly.

### 2019-07-27
Added circos diagrams where the line plots have window sizes of 100 and 500. Still haven't got the axes to work properly.

### 2019-08-05
Finally fixed the axis (on the window size 10 diagram) so that they are orientated outwards. The problem occurred because the line plots' positions are relative to the ideograms size, but I had written them relative to the whole image size available. Also made the .conf files neater and more compact, and did the same for the other window sizes.

Edited the python program that creates the karyotype, and created an accompanying circos file to create a plot where the colour of each gene depends on the table of the wiki page it was from. Each table contains data about genes that code for different things (proteins, rRNAs, tRNAs). I would like to use a [legend](http://circos.ca/documentation/tutorials/2d_tracks/heat_maps/) but it turns out circos doesn't yet use legends.

### 2019-08-06
Rewrote the generate_mtDNA_genome.py program so that it works by reordering the original genome. Wrote a function to do this then realised there was already a [shuffle function](https://smallbusiness.chron.com/randomize-list-python-26724.html) in the [random](https://docs.python.org/3/library/random.html) module, so I changed the code to use that instead. I also changed the plot_mtDNA.py program so that it plots all of the graphs and you don't have to manually keep on changing the paths.

Created the new images, and edited the post to include them, and say a bit about the difference between them.

Have been trying to get labels on the plot circos3, but haven't been able to get it to work. It turns out it was because I put an ordinary number for the position instead of using the 'r' suffix to indicate relative to ideogram size. Made a lot of small adjustments to the label positions so that they look good. I have now been trying to get labels for larger genes to be parallel to the circle. However I can't understand rules properly nd how to use them, or how to do comparisons with them.

###2019-08-07
Looked at downloading information using wget in python, and successfully downloaded a genome sequence in .fasta format.

Increased the thickness of the line plots in circos, then fixed an error where the data generated for use was from the random genome instead of the actual genome. Also removed uneccessary data points to reduce the time taken to generate images and the file size of the data files.
