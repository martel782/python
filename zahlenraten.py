#zahlenraten

import random
title = "Willkommen beim Zahlen-Raten_Spiel!"
print(title)
von = int(input("Bitte geben Sie den Ersten Wert des Zallenfeldes ein :"))
bis = int(input("Bitte geben Sie den zweiten und letzten Wert des Zallenfeldes ein: "))
zzahl=random.randint(von,bis)
i = 0;

text ="Bitte versuch meine Zahl zwischen",von,"und ",bis," zu raten"
eingabeText ="Dein Versuch"
counter = 0

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
