import pyopenms
from pyopenms import *

x = ModificationsDB().getModification("Oxidation")
print(x.getUniModAccession())
print(x.getUniModRecordId())
print(x.getDiffMonoMass())
print(x.getId())
print(x.getFullId())
print(x.getFullName())
print(x.getDiffFormula())