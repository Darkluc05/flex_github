import os


huidige_map = os.getcwd()

alle_bestanden = os.scandir(huidige_map)

print("Inhoudsopgave van de map: " + huidige_map)
for bestand in alle_bestanden:    
    if bestand.is_file():
        # Dit wordt uitgevoerd als dit een normale file is
        print(bestand.name + " (BESTAND)")
    elif bestand.is_dir():
        # Dit wordt uitgevoerd als dit een dir(ectory) is
        print(bestand.name + " (MAP)")
    else:
        # Dit wordt uitgeveord als het geen file en geen dir is
        print(bestand.name + " (ONBEKEND TYPE")