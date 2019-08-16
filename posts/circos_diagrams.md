# Circos diagrams
This post shows the diagrams that I have created using circos.

In order to create the diagrams you have to pass some parameters to a program I wrote. There are several parameters that affect the features present and the layout of the diagram, however all of the data is accessed using just the accession number of the genome you want. This means that once you have created a style of diagram you like, it is easy to create images for lots of different species.

There are 3 different species I have used here: Human, Mouse, and Baker's yeast. Which have accession numbers NC_012920.1, NC_005089.1, NC_027264.1, respectivley.

The images are in png format, however you can also get [svg images] if you want a vector graphics image, (the quality won't reduce if you zoom in).

Human:
<img src="../images/circos/NC_012920.1.png" alt="NC_012920.1">

Mouse:
<img src="../images/circos/NC_005089.1.png" alt="NC_005089.1">

Baker's yeast:
<img src="../images/circos/NC_027264.1.png" alt="NC_027264.1">

In the diagrams the inner circle section is the - strand, and the outer circle section is the + strand.

The different colours represent different genes, where genes that code for proteins are red, rRNAs are green, tRNAs are blue, the D-loop is grey, and the rest of the genome is white. All of the interesting genomic sections are also labelled.

Around the edge of the chromosome are [nucleobase proportion plots](mitochondrial_genome_plots.md) which use a window size of 100.

Unfortunately Circos doen't yet have a way to orientate labels outwards, so the - strand labels might seem a bit strange.
