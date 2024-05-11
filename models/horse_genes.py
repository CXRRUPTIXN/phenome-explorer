from enum import Enum

from models.genome import *

class AgoutiGene(Gene):
    class Alleles(Enum):
        DOMINANT = 'A'
        RECESSIVE = 'a'

    # Implement from parent class
    def isExpressed(self):
        # result = False
        # # Returns True if there is at least one DOMINANT gene
        # for a in self.allelePair:
        #     if a == self.Alleles.DOMINANT:
        #         result = True
        # return result
        return True # Agouti gene is always expressed

    def getGeneType(self):
        return InheritancePattern.DOMINANT

    def __init__(self):
        super()
        self.name = 'AGOUTI'
        self.allelePair = [
            self.Alleles.DOMINANT,
            self.Alleles.RECESSIVE
        ]

class HorseGenotype(Genotype):
    def __init__(self):
        self.genes = [
            # TODO Implement later
        ]
