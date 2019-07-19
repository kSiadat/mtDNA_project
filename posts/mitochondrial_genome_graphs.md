# Mitochondrial genome graphs

## What is a mitochondrial genome graph
'Mitochondrial genome graph' is not actually a proper term, what I mean is that I have created a graph that is to do with the mitochondrial genome.

It is essentially a graph, with a line for each base type, where the y-axis is the proportion of the mtDNA that is that base , within a certain section of the genome.

## Writing the code
In order to create the graphs, I first installed matplotlib, and looked up how to use it. To do that I had to edit the system path variable to add python because it was not already in the path.

The code consists of 3 main parts:

### Reading the mitochondrial genome
This section of the code was written by Conor.

First a list is created, where each item in the list is a line in the original file. List comprehension is a compact way of using a for loop to create a list, the function .readlines() is used to make the temporary variable of the for loop gold the value of each line of the file. The .rstrip() function removes whitespace from the right hand side of the line, which removes newline characters.

Then the first item (which would have been the first line of the list) is discarded because it contains header information. After that the .join() function is used to concatenate all of the remaining items together with "" (no gaps) in between each of them. 

### Finding a subsection of the genome
This code was also created by Conor.

Becuase mtDNA is circular, it is completely legitimate to look at a section that begins near the end of the genome string, and which ends near the start (essentially looping back to the start when the end is reached). So this function has 4 cases to deal with and uses an if statement for them. Which case it is depends on whether the start pointer is in or out of the normal indexing range of the genome string, and whether end pointer is in or out of that range.

### Plotting the graphs
This function takes genome, interval, and window as parameters. What it does, is it takes a sample of the genome every n bases where n is ther specified interval size, and uses a sample frame from n-x to n+x, where x is the specified window size. In order to obtain the sample frame it calls the subSeq function.

Then the proportion of each base is calculated by calling .count() on each sample frame using each base as a parameter, this counts the number of each base in the sample frame. Those values are then divided by the size of the sample frame, which is (2 x window size) + 1.

Next list comprehension is used to create a list x and y coordinates using what has already been calculated. These are then plotted as a seperate line for each base.

A legend is created and labels added to the axis.

Vertical lines are placed at the start and end of the genome string. This is because in a sample frame could go off the end and back to the start, so it would be useful to indicate when it does.

### Generating a random genome
For this code I had to get the length of the genome by putting a print statement in the graph program, then randomly select a base that many times and add it to a string.

Then I had to write it all to a file, leaving a an empty line at the start, so that when the reading program disacards the header it doesn't discard the actual information.

After that I added the path to the file in to the plotting program and created some graphs.

## Comparison
When looking at the graphs that have a small window size it is hard to see the difference between them because the data is so compressed and fluctuates so much that it is hard to take in.

However when looking at larger window sizes, you can see the difference. The randomly generated genome fluctuates a lot more than the actual genome, and in the actual genome some bases are more common than others on average, which is not true for the comlpetely random genome.
