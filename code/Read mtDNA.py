class mtDNA_genome():
    def __init__(self, path="data\\mtDNA.fa"):
        file = open(path, "r")
        lines = []
        for line in file.readlines():
            lines.append(line[:-1])
        file.close()
        self.genome = ""
        for x in range(len(lines)-1):
            self.genome += lines[x+1]

mtDNA = mtDNA_genome()
