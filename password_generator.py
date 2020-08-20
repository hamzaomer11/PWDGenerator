import random


upperAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I",  "J", 
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"
                 "U", "V", "W", "X", "Y", "Z"]



lowerAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"
                 + "u", "v", "w", "x", "y", "z"]

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ["£", "$", "%", "&", "*", "/"]

newAscii = upperAlphabet + lowerAlphabet + numbers + symbols

print(newAscii)

print("Do you want a new strong pasword?")
reply = input("Enter yes: ")


if reply == "yes" or reply == "y":
    print(random.sample(newAscii, 9))

elif reply == "no" or reply == "n":
    print("No new password")

