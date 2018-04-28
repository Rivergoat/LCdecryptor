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

countLetterFrequency()
