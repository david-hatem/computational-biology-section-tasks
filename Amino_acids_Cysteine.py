import pyopenms
from pyopenms import *
x = ResidueDB().getResidue("Cysteine")
print(x.getName())
print(x.getThreeLetterCode())
print(x.getOneLetterCode())
print(x.getAverageWeight())
print(x.getMonoWeight())
print(x.getPka())
print(x.getFormula().toString())