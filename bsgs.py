#!/usr/bin/python
from ctypes.wintypes import tagRECT
import sys, getopt
from turtle import clear

def pasSize(p):
    return round((p-1)**0.5)

def petitPas(g, mod, size):
    res = []
    for i in range(size):
        res.append(pow(g,i,mod))
    return res

def grandPas(g, mod, size):
    res = []
    for i in range(size):
        res.append(57*pow(g, - size * i , mod)%mod)
    return res


def main(argv):
    try:
        generator = int(argv[0])
        target = int(argv[1]) 
        modulus = int(argv[2])         
    except:
        print("To find x so generator^x=target[modulus]:\nbsgs.py <generator> <target> <modulus> ") 
    
    #PAS
    pas_size = pasSize(modulus)
    print(f"Step size = Round_up((modulus-1)**0.5) = {pas_size}\n")
    final_grand_pas = 0
    final_petit_pas = 0
    
    petit_pas = petitPas(generator, modulus, pas_size)
    print(f"Petit Pas => {generator}^j: \n\t{petit_pas}\n")
    grand_pas = grandPas(generator, modulus, pas_size)
    print(f"Grand Pas => {target}*{generator}^-{pas_size}*i:\n\t{grand_pas}\n")

    for i in grand_pas:
        for j in petit_pas:
            if i==j:
                final_grand_pas = grand_pas.index(i)
                final_petit_pas = petit_pas.index(j)
    final_exp=final_grand_pas *pas_size + final_petit_pas
    
    print(f"{generator}^({pas_size}*i+j) = {generator}^({pas_size}*{final_grand_pas}+{final_petit_pas}) = {generator}^{final_exp} = {target}\n")

    return final_exp

clear
if __name__ == "__main__":
   main(sys.argv[1:])
