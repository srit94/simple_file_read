#Works only in console, not in VSC. Because its another path then VCS gives as parameter

#dictionary in breakets {}
woerterEnDe = {}
woerterDeEn = {}

#with automatically close file when finish working with it
with open("woerterbuch.txt", "r") as oFile:
    for line in oFile:
        #equals trim in other languages. Removes line breaks
        line = line.strip()
        zuordnung = line.split(" ")
        if len(zuordnung) == 2: #is array of two?!
            woerterEnDe[zuordnung[0]] = zuordnung[1]
            woerterDeEn[zuordnung[1]] = zuordnung[0]

while True:
    word = input("Geben sie ihr Wort ein: ")
    if word == "end":
        break    
    
    if word in woerterEnDe: # checks if word 'english' contains in dictionary
        print("Das deutsche Wort lautet:", woerterEnDe[word])
    elif word in woerterDeEn: #check if word is german
        print("Das englische Wort lautet:", woerterDeEn[word])
    else:
        print("Das Wort ist unbekannt")