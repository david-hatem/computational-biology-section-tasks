import pyopenms
from pyopenms import *
s = AASequence.fromString("DFPIANGER")

print("The peptide ", str(seq), " consists of the following amino acids:")
for i in s:
    print(i.getName(), ":", i.getMonoWeight())