from enum import Enum, auto
from abc import abstractmethod

class InheritancePattern(Enum):
    DOMINANT = auto()
    RECESSIVE = auto()
    CO_DOMINANT = auto()

class AlleleType(Enum):
    DOMINANT = auto()
    RECESSIVE = auto()

# Individual genetic traits - two of these together make up a Gene
class Allele:

    def __init__(self, gene, character):
        self.gene = gene
        return

# Combined pair of alleles, e.g. Aa
class Gene:
    # Function that returns a list of Allele objects based on provided alleleString
    # Inherited by all children of Gene
    def getAllelesFromString(self, alleleString):
        name = ''
        alleles = []
        for s in alleleString:
            name += s
            # Check if name matches any of this gene's allele types
            for a in self.Alleles:
                if a.value == name:
                    alleles.push(a)
                    name = ''
                    break # Jump out of for loop
                    
    # Returns inheritance type of this gene - dominant, recessive, co-dominant, etc.
    @abstractmethod
    def getGeneType(self):
        pass

    # A simple True/False bool determining whether this gene is expressed in the phenotype
    @abstractmethod
    def isExpressed(self):
        pass # TODO Make this default to False

    @property # (I hope I'm using this correctly)
    def geneString(self): # TODO This may or may not be extraneous
        result = ''
        for a in self.allelePair:
            # TODO Sort this so dominant alleles sort in front of recessive ones
            result += a.value
        return result

    def __init__(self, alleleString=False):
        self.name = ''
        self.type = self.getGeneType()
        if alleleString: # If alleleString exists, get alleles from that
            self.alleles = self.getAllelesFromString(alleleString)
        else:            # Else, we'll figure it out later
            self.alleles = [] # TODO Placeholder

class Genotype:

    # TODO Returns the organism's phenotype as a string
    def calculateFullPhenotype(self, genes):
        return ''
    
    def __init__(self):
        # An array containing all relevant genes
        self.genes = []

        self.phenotype = self.calculateFullPhenotype(self.genes)


# p = Genotype()