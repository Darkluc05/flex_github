import os

bestandsnaam = "demobestand.txt"

huidige_map = os.getcwd()

volledige_pad = os.path.join(huidige_map, bestandsnaam)
print("Dit bestand gaan we hernoemen: " + volledige_pad)

valid_input = False
while not valid_input:
    nieuwe_naam = input("Nieuwe bestandsnaam: ")
    if len(nieuwe_naam) > 0:
        nieuwe_volledige_pad = os.path.join(huidige_map, nieuwe_naam)
        print("Bestand wordt hernoemd naar: " + nieuwe_volledige_pad    )

        os.rename(volledige_pad, nieuwe_volledige_pad)
        print("Bestand hernoemd")
        valid_input = True
    else:
        print("Sorry, geen geldige invoer, einde programma")