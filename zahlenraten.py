#zahlenraten

import random
zzahl=random.randint(1,1000)
i = 0;
title = "Willkommen beim Zahlen-Raten_Spiel!"
text ="Bitte versuch meine Zahl zwischen 1 und 1000 zu raten"
eingabeText ="Dein Versuch"
counter = 0
print(title)
print(text)
#uzahl = int(input(eingabeText))      
fertig = False

while (fertig == False):
        uzahl = int(input(eingabeText))
        counter = counter + 1
        if(zzahl == uzahl):
                print("gewonnen")
                fertig = True
        elif(uzahl < zzahl):
                print("Deine Zahl ist zu klein")
        else:
                print("Deine Zahl ist zu groß")



print("super du hast dafür nur ",counter," Versuche benötigt")
print("ende")
        
