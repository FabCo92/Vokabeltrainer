import json

#Basis bildet alle möglichen Vokabeln und wird nicht verändert

#Basis Dictonary und 1a) durch serialisierung nicht mehr nötig
# basis = {"Ausgabe" : "print()",
#             "Wenn-Dann-Anweisung" : "if",
#             "Schleife1" : "for",
#             "Schleife2" : "while",
#             "Länge einer Liste" : "len()",
#             "Eingabe" : "input()",
#             "Integer-Umwandlung" : "int()",
#             "Gleitkommazahl-Umwandlung" : "float()",
#             "Zeichenketten-Umwandlung" : "str()",
#             "Liste l deklarieren" : "l = []",
#             "Tupel t deklarieren" : "t = ()",
#             "Dictionary d deklarieren" : "d = {}",
#             "boolean für wahr" : "True",
#             "boolean für falsch" : "False",
#             "Vergleichsoperator bei Gleichheit" : "==",
#             "Vergleichsoperator bei Ungleichheit" : "!=",
#             "Logische Und-Verkünpfung" : "and",
#             "Logische Oder-Verknüpfung" : "or",
#             "Logischer Nicht-Operator" : "not",
#             "Funktionsdefinition" : "def",
#             "Rückgabe-Befehl" : "return",
#             "Runden einer Zahl" : "round()"}


# 1b) Stufen
# Stufe 1 Dictonary ist Grundlage und Kopie aller Vokabeln
# nicht mehr gebraucht
# tier1 = basis.copy()
# 
# # Stufe 2 Dictonary
# tier2 = {}
# 
# # Stufe 3 Dictonary
# tier3 = {}
# 
# # Stufe 4 Dictonary
# tier4 = {}
# 
# # Stufe 5 Dictonary
# tier5 = {}
# 
# # Finish Dictonary
# finish = {}

# 1c) Dictonary mit Punkten erstellen
#punkteDict = {}
# füllt das Dictonary mit allen keys aus basis
# for keys in basis:
#     punkteDict[keys] = 0


###########################################
##### Hier beginnt das fertige Program ####
###########################################



def abspeichernRanks(punkteDict):
    vokabelheft_ranks = json.dumps(punkteDict,indent = 4)
    with open("vokabelheft_rank.txt", "w") as outfile:
        outfile.write(vokabelheft_ranks)
        
def abspeichernVokabeln(basis):
    vokabelheft_keys = json.dumps(basis,indent = 4)
    with open("vokabelheft_keys.txt", "w") as outfile:
        outfile.write(vokabelheft_keys)

def neuerEintrag(basis,punkteDict):
    userInput = input("Wollen Sie einen neuen Eintrag ins Vokabelheft hinzufügen? J/N ")
    if userInput == "J" or userInput == "j":
        newKey = input("Neue Abfragevokabel: ")
        if newKey in basis:
            print("Diese Vokabel exsitiert bereits")
            neuerEintrag()
        else:
            newValue = input("Richtige Lösung: ")
            # initiiert neue Vokabel in dicts
            basis[newKey] = newValue
            punkteDict[newKey] = 0
            abspeichernRanks(punkteDict)
            abspeichernVokabeln(basis)
            neuerEintrag(basis, punkteDict)
    elif userInput == "N" or userInput == "n":
        print("Programm beendet")
        exit()
    else:
        print("Ungültige Eingabe")
        neuerEintrag()
        
            
def start():
    #Dictonary mit Vokabeln laden
    with open('vokabelheft_keys.txt', 'r') as openfile:
        basis = json.load(openfile)
    
    #Dictonary mit Bewertungen laden
    with open('vokabelheft_rank.txt', 'r') as openfile:
        punkteDict = json.load(openfile)
    
    #Bestimmt wieviele Vokabeln gelernt werden soll
    n = input("Wähle aus wieviele Vokabeln gelernt werden sollen: ")
    #darf natürlich nicht mehr sein, als es im Dict gibt
    if int(n) > len(punkteDict):
        #Fehlermeldung
        print("So viele Vokabeln befinden sich nicht im Vokabelheft")
        #fliegt ausm Programm
        return

    #sortiert das Dict nach values aufsteigend
    sortedDict = sorted(punkteDict.items(), key=lambda x: x[1], reverse=False)
    
    
    print(5*'*',"Abfrage von ",n," Vokabeln beginnt",5*'*')
    print()
    
    #iteriert solange bis gewünschte Anzahl erreicht ist
    for i in range(int(n)):
        #fordert eingabe für erste Vokabel
        eingabe = input(str(sortedDict[i][0]) + ": ")
        #Wenn sie richtig ist (sortedDict ist eine Liste von Tupeln, darum zwei Indices)
        if eingabe == basis[sortedDict[i][0]]:
            print("Richtig!")
            #Erhöhung des Values um 1
            punkteDict[sortedDict[i][0]] += 1
        #Abbrucheingabe "Nein"
        elif eingabe == "Nein":
            #Vor Exit abspeichern
            abspeichernRanks(punkteDict)
            exit()
        else:
            print("Leider Falsch")
            
    #abseichern
    abspeichernRanks(punkteDict)
    #nach der Schleife weitere Optionen
    print("Test beendet")
    restart = input("Wollen Sie erneut starten? J/N ")
    if restart == "J" or restart == "j":
        start()
    elif restart == "N" or restart == "n":
        neuerEintrag(basis,punkteDict)
        
# Hier stand die Lösung für 1b)
# def start():
#     # Programmausführung
#     for key in list(tier1):
#         eingabe = input(key + ":")
#         #Bei richtiger Eingabe
#         if tier1[key] == eingabe:
#             print("Richtig! " + key +" -> " + basis[key] + " ist nun in Stufe 2" )
#             #löscht aus basis
#             tier1.pop(key)
#             tier2[key] = eingabe
#         #Abbruch    
#         elif eingabe == "Nein":
#             exit()
#         
#         #bei falscher Eingabe
#         else:
#             print("Leider Falsch!")
#     
#     for key in list(tier2):
#         eingabe = input(key + ":")
#         #Bei richtiger Eingabe
#         if tier2[key] == eingabe:
#             print("Richtig! " + key +" -> " + tier2[key] + " ist nun in Stufe 3" )
#             #löscht aus basis
#             tier2.pop(key)
#             tier3[key] = eingabe
#         #Abbruch    
#         elif eingabe == "Nein":
#             exit()
#         
#         #bei falscher Eingabe
#         else:
#             print("Leider Falsch!")
#     
#     for key in list(tier3):
#         eingabe = input(key + ":")
#         #Bei richtiger Eingabe
#         if tier3[key] == eingabe:
#             print("Richtig! " + key +" -> " + tier3[key] + " ist nun in Stufe 4" )
#             #löscht aus basis
#             tier3.pop(key)
#             tier4[key] = eingabe
#         #Abbruch    
#         elif eingabe == "Nein":
#             exit()
#         
#         #bei falscher Eingabe
#         else:
#             print("Leider Falsch!")
#     
#     for key in list(tier4):
#         eingabe = input(key + ":")
#         #Bei richtiger Eingabe
#         if tier4[key] == eingabe:
#             print("Richtig! " + key +" -> " + basis[key] + " ist nun in Stufe 5" )
#             #löscht aus basis
#             tier4.pop(key)
#             tier5[key] = eingabe
#         #Abbruch    
#         elif eingabe == "Nein":
#             exit()
#         
#         #bei falscher Eingabe
#         else:
#             print("Leider Falsch!")
#             
#     for key in list(tier5):
#         eingabe = input(key + ":")
#         #Bei richtiger Eingabe
#         if tier5[key] == eingabe:
#             print("Richtig! Letzte Stufe geschafft! Vokabel erneut lernen?")
#             tier5.pop(key)
#             neu = input("Ja/Nein")
#             if neu == "Ja":
#                 tier1[key] = eingabe
#             elif neu == "Nein":
#                 finish[key] = eingabe
#             else: 
#                 print("Ungültige Eingabe")
#         #Abbruch    
#         elif eingabe == "Nein":
#             exit()
#         
#         #bei falscher Eingabe
#         else:
#             print("Leider Falsch!")
        
# Start
def anfang():
    beginn = input("Zum Start der Anwendung schreiben sie start: ")
    if beginn == "start":
        start()
    else:
        print("Ungültige Eingabe")
        anfang()
    

# Einführung
print()
print(41*"*")
print(4*"*","Willkommen beim Vokabeltrainer!",4*"*")
print(41*"*")
print()
anfang()




            