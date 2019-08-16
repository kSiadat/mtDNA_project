from mtdna_utilities import empty_folder, get_genome, write_file
from create_line_plot_data import create_linePlot_data
from get_gene_data import get_gene_data
import os

def create_ideogram(radius=0.6, thickness=0.075):
    conf_ideogram = f"""
        <ideogram>
            <spacing>
                default = 0r
            </spacing>

            show_bands            = yes
            fill_bands            = yes
            band_stroke_thickness = 2p
            ban_stroke_colour     = black

            radius           = {radius}r
            thickness        = {thickness}r
            fill             = yes
            stroke_color     = black
            stroke_thickness = 2p
        </ideogram>
    """
    """
        <ideogram>
            <spacing>
                default = 0r
            </spacing>

            show_bands            = yes
            fill_bands            = yes
            band_stroke_thickness = 2p
            ban_stroke_colour     = black

            radius           = {radius-thickness-0.1}r
            thickness        = {thickness}r
            fill             = yes
            stroke_color     = black
            stroke_thickness = 2p
        </ideogram>
    """
    return conf_ideogram


def create_image(path="../images/circos", fileName="circos"):
    conf_image = f"""
    <image>
        dir*  = {path}
        file* = {fileName}
        <<include etc/image.conf>>                
    </image>
    """
    return conf_image


def create_axes(data):
    #Data in format [[spacing, colour], [spacing, colour]]
    if data!=None:
        conf_axes = "<axes>\n"
        for D in data:
            conf_axes += f"<axis>\n spacing={D[0]}\n color={D[1]}\n </axis>\n"
        conf_axes += "</axes>\n"
        return conf_axes


def create_ticks(radius, orientation, label_interval):
    if not radius[-1].isalpha():
        radius += "r"
    return f"""
    show_ticks       = yes
    show_tick_labels = yes
    <ticks>
    radius           = {radius}
    orientation      = {orientation}
    color            = black
    thickness        = 2p

    multiplier       = 1
    format           = %d

    <tick>
    spacing        = 0.1u
    size           = 10p
    </tick>

    <tick>
    spacing        = 1u
    size           = 20p
    </tick>

    <tick>
    spacing        = {label_interval}u
    size           = 20p
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    label_parallel = yes
    format         = %d
    </tick>

    </ticks>
    """


def create_plots(data):
    #Data in format [[type=text, file, r0, r1],  [type=line, file, r0, r1, min, max, color, axes, [accession, path, windows]]
    conf_plots = "<plots>\n"
    for D in data:
        conf_plots += f"<plot>\n type = {D[0]}"
        if D[0] == "text":
            conf_plots += f"""
            file        = {D[1]}
            r0          = {D[2]}r
            r1          = {D[3]}r
            label_font  = sans_serif
            color       = black
            label_size  = 40p

    	    show_links     = {D[4]}
	    link_color     = black
	    link_dims      = 5p, 10p, 20p, 10p, 5p
	    link_thickness = 3p

	    label_snuggle                  = yes
	    max_snuggle_distance           = 10r
	    snuggle_sampling               = 2
	    snuggle_tolerance              = 1r
	    snuggle_link_overlap_test      = yes 
	    snuggle_link_overlap_tolerance = 2p
	    snuggle_refine                 = yes
	    """

        if D[0] == "line":
            if D[8]!=None:
                create_linePlot_data(D[8][0], D[8][1], D[8][2])
            conf_plots += f"""
            file      = {D[1]}
            r0        = {D[2]}r
            r1        = {D[3]}r
            min       = {D[4]}
            max       = {D[5]}
            color    = {D[6]}
            thickness = 2p
            """
            if D[7]!=None:
                conf_plots += f"{create_axes(D[7])}\n"

        if D[0] == "tile":
            conf_plots += f"""
            file       = {D[1]}
            r0         = {D[2]}r
            r1         = {D[3]}r
            orientaion = out
            layers     = 1
            margin     = 0b
            thickness  = {thickness*1000}
            padding    = 0
            stroke_thickness = 2p
            stroke_color     = black
            """
        conf_plots += "</plot>\n"
    conf_plots += "</plots>\n"
    return conf_plots


#accession = "NC_012920.1" # Human reference sequence
#accession = "NC_005089.1" # Mouse reference sequence
#accession = "NC_027264.1" # Baker's yeast (Saccharomyces cerevisiae) reference sequence
accession = "NC_001224.1" # Another yeast

path = "../data/temp/"
ideoDims = [0.6, 0.075]
thickness = ideoDims[1]/ideoDims[0]
genomeLength = len(get_genome(accession))

conf_ideogram = create_ideogram(ideoDims[0], ideoDims[1])
conf_image = create_image("../images/circos", accession)
conf_plots = ""
conf_ticks = ""

if genomeLength < 30000:
    conf_ticks = create_ticks(f"{1-thickness}r+10p", "out", 1)
else:
    conf_ticks = create_ticks(f"{1-thickness}r+10p", "out", 5)

get_gene_data(accession, path)
plots = [["text", f"{path}karyotype.{accession}.+.band_labels.txt", 1, 1.25, "yes"],
         ["text", f"{path}karyotype.{accession}.-.band_labels.txt", 0.78-(2*thickness), 0.98-(2*thickness), "no"],
         ["tile", f"{path}karyotype.{accession}.-.txt", 0.98-(2*thickness), 0.98-thickness]]
bases = ["A", "C", "G", "T"]
colours = ["blue", "orange", "green", "red"]
for x in range(len(bases)):
    temp = ["line", f"{path}{accession}_linePlot_100_{bases[x]}.txt", 1.27, 1.65, 0, 0.5, colours[x], None, None]
    if x==0:
        temp[7] = [[0.1, "grey"], [0.5, "vdgrey"]]
        temp[8] = [accession, path, [100]]
    plots.append(temp)
conf_plots = create_plots(plots)

main = f"""
karyotype = {path}karyotype.{accession}.+.txt

chromosomes_units = 1000

{conf_ideogram}
{conf_image}
{conf_plots}
{conf_ticks}

<<include etc/colors_fonts_patterns.conf>> 
<<include etc/housekeeping.conf>>
"""

write_file("circos.conf", main)
os.system("circos -conf circos.conf -noparanoid")
empty_folder(path)
