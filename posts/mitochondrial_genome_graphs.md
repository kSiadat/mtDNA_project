# Mitochondrial genome graphs

## What is a mitochondrial genome graph
'Mitochondrial genome graph' is not actually a proper term, what I mean is that I have created a graph that is to do with the mitochondrial genome.

The genome is essentially a long list of bases. The x-axis just represents a position in the genome.

The y-axis is the proportion of a certain section of the genome that is each base. Each section is an area of the genome based on an index and window size. The index is the x-axis value, and the window size is specified when creating the graph. The section is from index - window to index + window.

## Comparing different graphs
Each graph is created from 1 of 2 sets of data. There is the actual genome, which is a real mitochondrial genome that has been sequenced, and then there is the randomly genereated genome I created in order to compare to the actual genome to see if there would be much difference.

Each graph also differs in terms of interval (the distance between each sample) and window size.




When looking at the graphs that have a small window size, it is hard to understand the information properly because the lines fluctuate so much between each index position, and there are so many indexes represented in a relativley small space. So it looks very cramped and is hard to take in, which makes it impossible to tell the difference between the randomly generated and actual genomes.

However when looking at larger window sizes, you can see more interesting patterns, and the . The randomly generated genome fluctuates a lot more than the actual genome, similarly to when looking at smaller window sizes, and in the actual genome some bases are more common than others on average, which is not true for the comlpetely random genome.
