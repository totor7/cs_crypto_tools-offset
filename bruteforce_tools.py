#!/usr/bin/python

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#BRUTEFORCE FUNCTIONS
def stats(x):
    occurrences = 26*[0]
    #Count
    for i in x:
        occurrences[alphabet.index(i)]+=1
    #Normalize
    for o in range(len(occurrences)):
        occurrences[o] = occurrences[o] / len(x)
    return occurrences

def MIC(x,y):
    sum = 0
    xStats = stats(x)
    yStats = stats(y)
    for i in range(len(alphabet)):
        sum += xStats[i]*yStats[i]
    return sum 

def IC(x):
    return MIC(x,x)

def guessKeyLength(cipher):
    ic = 0
    l=0
    while ic < 0.07:
        l+=1
        subset = cipher[::l]
        ic = IC(subset)
    return l

