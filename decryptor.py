def countLetterFrequency(text = "test"):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Q","Y","Z"]
    occurrence = []

    for i in range(26 * 2):
        occurrence.append(0)

    for i in range(len(text)):
        for l in range(len(letters)):
            if text[i] == letters[l]:
                occurrence[l] += 1

    return occurrence

def writeToFile(text, filename = "decryptedtxt.txt"):
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
        if printInfo == True: print("Successfully read line", i+1, "in", filename)
    txt.close()

    return content

def decrypt():
    encryptedText = readFromFile("encryptedtxt.txt")
    sampleText    = readFromFile("txt.txt")

    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    translator1Letters = []
    translator2Letters = []

    for i in range(26 * 2):
        translator1Letters.append("placeholder")
        translator2Letters.append("placeholder")

    decryptedText = " "

    occurenceInEncrpdTxt = countLetterFrequency(encryptedText)
    occurenceInSampleTxt = countLetterFrequency(sampleText)

    orderInEncrpdTxt = []
    orderInSampleTxt = []

    for i in range(26 * 2):
        biggestFound = 0
        itsNumber = 0

        for l in range(26 * 2):
            if occurenceInEncrpdTxt[l] > biggestFound:
                itsNumber = l
                biggestFound = occurenceInEncrpdTxt[l]

        occurenceInEncrpdTxt[itsNumber] = 0
        orderInEncrpdTxt.append(itsNumber)

    for i in range(26 * 2):
        biggestFound = 0
        itsNumber = -1

        for l in range(26 * 2):
            if occurenceInSampleTxt[l] > biggestFound:
                itsNumber = l
                biggestFound = occurenceInSampleTxt[l]

        occurenceInSampleTxt[itsNumber] = 0
        orderInSampleTxt.append(itsNumber)

    for i in range(26 * 2):
        ithLetterInSample = letters[orderInSampleTxt[i]]

        itsNumberInEncprd = 0

        for l in range(26 * 2):
            if letters[orderInEncrpdTxt[l]] == ithLetterInSample:
                itsNumberInEncprd = l
                break

        translator1Letters[itsNumberInEncprd] = letters[orderInSampleTxt[i]]
        letters

    for i in range(26 * 2):
        translator2Letters[i] = letters[orderInSampleTxt[i]]

    foundMatch = False

    for c in range(len(encryptedText)):
        for a in range(len(letters)):
            if encryptedText[c] == translator1Letters[a]:
                decryptedText += translator2Letters[a]
                foundMatch = True
                break

        if foundMatch == False:
            decryptedText += encryptedText[c]

        foundMatch = False

    return decryptedText



def printArray(array):
    for i in range(len(array)):
        print(array[i])

def printArrayWithLetter(array):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Q","Y","Z"]

    for i in range(26 * 2):
        print((i+1)," ", letters[array[i]])


writeToFile(decrypt())
