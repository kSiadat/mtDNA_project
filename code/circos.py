from mtdna_utilities import write_file

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
        stroke_thickness = 0p
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


def create_plots(data):
    #Data in format [[type=text, file, r0, r1],  [type=line, file, r0, r1, min, max, color, axes]]
    conf_plots = "<plots>\n"
    for D in data:
        conf_plots += "<plot>\n type = D[0]"
        if D[0] == "text":
            conf_plots += f"""
            file       = {D[1]}
            r0         = {D[2]}r
            r1         = {D[3]}r
            label_font = sans_serif
            color      = black
            label_size = 40p

    	    show_links     = yes
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
            conf_plots += f"""
            file      = {D[1]}
            r0        = {D[2]}r
            r1        = {D[3]}r
            min       = {D[4]}
            max       = {D[5]}
            color    = {D[6]}
            thickness = 2p
            {create_axes(D[7])}
            """
        conf_plots += "</plot>\n"
    conf_plots += "</plots>\n"
    return conf_plots


accession = "NC_012920.1"

conf_ideogram = create_ideogram(0.6, 0.075)

conf_image = create_image("../images/circos", "circos1")

plots = [["text", "../data/karyotype.NC_012920.1.band_labels.txt", 1, 1.2]]
bases = ["A", "C", "G", "T"]
colours = ["blue", "orange", "green", "red"]
for x in range(len(bases)):
    plots.append(["line", f"../data/{accession}_linePlot_100_{bases[x]}.txt", 1.22, 1.6, 0, 0.5, colours[x], [[0.1, "grey"], [0.5, "vdgrey"]]])
conf_plots = create_plots(plots)

main = f"""
karyotype = ../data/karyotype.{accession}.txt

chromosomes_units = 1000000

{conf_ideogram}
{conf_image}
{conf_plots}

<<include etc/colors_fonts_patterns.conf>> 
<<include etc/housekeeping.conf>>
"""

write_file("circos.conf", main)