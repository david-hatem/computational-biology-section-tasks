import pyopenms

from pyopenms import *

edb = ElementDB()
oxygen_isoDist = {"mass": [], "abundance": []}


oxygen = edb.getElement("O")

isotopes = oxygen.getIsotopeDistribution()

for iso in isotopes.getContainer():

    print ("Oxygen isotope", iso.getMZ(), "has abundance",iso.getIntensity()*100, "%")

    oxygen_isoDist["mass"].append(iso.getMZ())

    oxygen_isoDist["abundance"].append((iso.getIntensity() * 100))






