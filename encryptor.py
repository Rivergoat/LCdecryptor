import time

def nextAlphabetLetter(text = "test"):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Q","Y","Z","A"]
    newText = " "
    foundMatch = False

    for l in range(len(text)):

        for a in range(len(letters)):
            if text[l] == letters[a]:
                newText += letters[a + 1]
                foundMatch = True
                break

        if foundMatch == False:
            newText += text[l]

        foundMatch = False

    return newText


testText = "abc"

def writeToFile(text, filename = "scrtxt.txt"):
    txt = open(filename, "w")
    txt.write(text)
    txt.close()

def linesOfFile(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass

    return i + 1

def readFromFile(filename = "txt.txt", printInfo = False):
    txt = open(filename, "r")
    content = " "
    for i in range(linesOfFile(filename)):
        content += txt.readline()
        if printInfo == True: print("Successfully read line", i+1)
        #time.sleep(0.001)
    txt.close()

    return content

writeToFile(nextAlphabetLetter(readFromFile("txt.txt", True)))
