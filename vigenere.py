#!/usr/bin/python
from cgi import print_directory
import sys, getopt
from traceback import print_tb
from turtle import clear
from bruteforce_tools import *
import cesar
#from turtle import clear

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
input = "aejifurocdjabmwrncgxvrjifjpolwvrrywceqixderoyvbwyyriaypuubytefwxpceihpwizfpsishgzvohevqicdvrsppzlzyluegfpedsglzngkfzcvuykebndfugfpjozytccsmevlzybleziydahllhuskfvlchafufmfzteopcobncrqiynvshywceeotjegifcejybligifwffypkssgpkebacvvswpjtsfwvqiiyvmdltjobhphucheiavcehuchlsabxzenskfzncoduobhpvnjcpuejcgieeotuobhpvnjcpuezudlijlpaugkfrupifkjimblaivzltxygfurllzsguyjlohzdmslwlifyyursbzdmoapaozcpwlsocuuaitjdsglzoizclihmllvoaplnsjwrnhymzebjwrnhypjufmpjdsoiaaavpjehkfztfuteeshwzbslevoivzelicdvmpfptegnpclskfvlchxrtfubleeopcobjzlrgotkqiywfnhllhuswpjtsfwvqicdvscowvvskfzscoqwrsyejeayevnulpmeqydkezfphuchpdpfcdfnbyblobncrhwnblobumrnriyeeeoteoimofnbypevwyovvwpcvqicofnbypevwyovlomfzvfyulseollbcoeaugkfrupifkjspzldfutjsohdcabixdefpzlsduccefxpclsvtvnocxvecoxrlocxvesfwvegnqzdsfpvtgcgfugpzllstblexygfugflgrsmpetsiycadjpclslpmoZoeZobjpimohpetswpjtsfwvqiywfnaueiaeophusfzepcocjuwnbleziykrokfvcsmevlzybligydfuzygvqicdfutzcvehmpdehyyxrspptegnpclskffnsgaiigiyeeeozetfuszteozeapuyuobhphuwhzlsriyeeshgzerygzvfybliriyeeshgzerywrsicgiexodhuoomfuhdfjqiufsoin"
input=input.lower()
# print(input)
def beautifier(list):
    toString=""
    for i in list:
        toString += i
    return toString

def encode(clearText, key, decode=1):
    cipherText = []
    keyValue = 0
    clearText = [o.lower() for o in clearText]
    for i in range(len(clearText)):
        if clearText[i].lower() in alphabet:
            oldIndex = alphabet.index(clearText[i].lower())
            keyIndex = alphabet.index(key[keyValue].lower())
            new_Index = (oldIndex + keyIndex*decode) % 26
            cipherText.append(alphabet[new_Index])
            keyValue = (keyValue + 1) % len(key)
    return cipherText

def decode(cipher, key):
    return(encode(cipher, key, -1))

def bruteforce(ciphertext):
    res = []
    ciphertext = [o.lower() for o in ciphertext]
    key_length=guessKeyLength(ciphertext)
    cesar_keys=[0]
    y0=ciphertext[::key_length]
    print(key_length)
    for i in range(1, key_length):
        yi = ciphertext[i::key_length]
        for ki in range(26):
            if(MIC(y0,cesar.decode(yi,ki)) > 0.07):
                cesar_keys.append(ki)
    for k in range(26):
        key_candidate =  "".join([ alphabet[(o+k)%26] for o in cesar_keys])
        print(f"With key: {key_candidate}\n")
        res.append([key_candidate,"".join(decode(ciphertext, key_candidate))])
        print(res[-1][-1])
        print("\n----------------------------------------------------------------------\n")

    return res

def main(argv):
    res=[]
    try: 
        if argv[0] == "d":
            res = decode([*argv[1]], [*argv[2]])
            print(beautifier(res))
        
        elif argv[0] == "e":
            res = encode([*argv[1]], [*argv[2]])
            print(beautifier(res))

        elif argv[0] == "b":
            res = bruteforce([*argv[1]])
    except:
        print("Standard : vigenere.py {d (decode), e (encode)} <string> <key>\nBruteforce: vigenere.py b <string>")

    return res

if __name__ == "__main__":
   main(sys.argv[1:])