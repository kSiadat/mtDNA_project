bases = ["A", "C", "G", "T", "N"]

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
        self.genome_length = len(self.genome)
        print(self.genome)

    def get_bases(self, start, end):
        def limit(num):
            while num > self.genome_length:
                num+=self.genome_length
            while num < 0:
                num =+ self.genome_length
            return num
        total = [0, 0, 0, 0, 0]
        start = limit(start)
        end = limit(end)
        if end <= start:
            for x in range(self.genome_length - start):
                total[bases.index(self.genome[x+start])] += 1
            for x in range(end + 1):
                total[bases.index(self.genome[x])] += 1
        else:
            for x in range(end + 1 - start):
                if not self.genome[x+start] in bases:
                    print(x, self.genome[x+start])
                total[bases.index(self.genome[x+start])] += 1
        proportion = []
        for X in total:
            proportion.append(X / (end + 1 - start))
        return proportion

mtDNA = mtDNA_genome()
print(mtDNA.get_bases(0, mtDNA.genome_length-1))
