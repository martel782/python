

def readDataSet(filename):
 
    fr = open(filename)                 # Datei-Stream vorbereiten
 
    numberOfLines = len(fr.readlines()) # Anzahl der Zeilen ermitteln
 
    returnMat = numpy.zeros((numberOfLines-1,3)) # Eine Numpy-Matrix in Höhe der Zeilenanzahl (minus Kopfzeile) und in Breite der drei Merkmal-Spalten
 
    classLabelVector = [] # Hier werden die tatsächlichen Kategorien (Haus, Wohnung, Büro) vermerkt
    classColorVector = [] # Hier werden die Kategorien über Farben vermerkt (zur späteren Unterscheidung im 3D-Plot!)
    
    #print(returnMat)   # Ggf. mal die noch die ausge-null-te Matrix anzeigen lassen (bei Python 2.7: die Klammern weglassen!)
    
    fr = open(filename) # Datei-Stream öffnen
    index = 0
    
    for line in fr.readlines():  # Zeile für Zeile der Datei lesen
        if index != 0:           # Kopfzeile überspringen
            line = line.strip()
            listFromLine = line.split('\t') # Jede Zeile wird zur temporären Liste (Tabulator als Trennzeichen)
 
            returnMat[index-1,:] = listFromLine[1:4] #Liste in die entsprechende Zeile der Matrix überführen
            
            classLabel = listFromLine[4]  # Kategorie (Haus, Wohnung, Büro) für diese Zeile merken
            
            if classLabel == "Buero":
                color = 'yellow'
            elif classLabel == "Wohnung":
                color = 'red'
            else:
                color = 'blue'
                        
            classLabelVector.append(classLabel) # Kategorie (Haus, Wohnung, Büro) als Text-Label speichern
            classColorVector.append(color)      # Kategorie als Farbe speichern (Büro = gelb, Wohnung = rot, Haus = Blau)
        
        index += 1
 
 
return returnMat,classLabelVector, classColorVector
