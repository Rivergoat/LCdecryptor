# LCdecryptor
This is an algorithm to encrypt text files, that are just encrypted by changing the letters in some way. For example changing every letter to the next in the alphabet. The program will use the different frequency of the letters. This will not be the must efficient method. Using a dictionary would be must better. The encrypted text needs to be long to ensure that the frequency matches the average.

A short explanation on how the project is structured:

encryptor.py        is the script to generate text, that I can test the algorithm.
encryptedtxt.txt    is the file containing the encrypted text. (It will be a encrypted version a txt.txt at first. I will use a different text when get it working with that.)

txt.txt             is a file containing a text to get the data about the occurrence of the letters. (I will get the content manually at first, but I may automate that by using some API to access a big amount of text at once.)

decrypor.py         is the decryptor, which will use txt.txt and scrtxt.txt and generate a  unscrtxt.txt with the best guess inside.
decryptedtxt.txt    is the output of decryptor.py.
