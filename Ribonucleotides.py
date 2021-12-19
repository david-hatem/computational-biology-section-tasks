import pyopenms
from pyopenms import *

u = RibonucleotideDB().getRibonucleotide(b"U")
print(u.getName())
print(u.getCode())
print(u.getAvgMass())
print(u.getMonoMass())
print(u.getFormula().toString())
print(u.isModified())
methyladenosine = RibonucleotideDB().getRibonucleotide(b"m1A")
print(methyladenosine.getName())
print(methyladenosine.isModified())