import pyopenms

from pyopenms import *

edb = ElementDB()


edb.hasElement("O")



oxygen = edb.getElement("O")

print(oxygen.getName())

print(oxygen.getSymbol())

print(oxygen.getMonoWeight())

print(oxygen.getAverageWeight())


print ("One mole of oxygen weighs", 2*oxygen.getAverageWeight(), "grams")

print ("One mole of 16O2 weighs", 2*oxygen.getMonoWeight(), "grams")