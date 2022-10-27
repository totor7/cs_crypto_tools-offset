#!/usr/bin/python
import sys
from unidecode import unidecode

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def beautifier(list):
    toString=""
    for i in list:
        toString += i
    return toString

def encode(clearText, key):
    cipherText = []
    for i in range(len(clearText)):
        if clearText[i].lower() in alphabet: 
            cipherText.append(alphabet[(alphabet.index(clearText[i].lower())+key)%26])
    return(beautifier(cipherText))

def decode(cipher, key):
    return encode(cipher, -key)

def bruteforce(text):
    res=[]
    for i in range(25):
        res.append(decode(text, i))
    return res

def main(argv):
    res=[]
    try:
        if argv[0] == "d":
            res=decode(unidecode(str([*argv[1]])), int(argv[2]))
            print(res)      
        elif argv[0] == "e":
            res=encode(unidecode(str([*argv[1]])), int(argv[2]))
            print(res)

        elif argv[0] == "b":
            res=bruteforce(unidecode(str([*argv[1]])))
            print("\n".join(res))
    except:
        print("Standard : cesar.py {d (decode), e (encode)} <string> <key>\nBruteforce: cesar.py b <string>")    

    return res

if __name__ == "__main__":
   main(sys.argv[1:])