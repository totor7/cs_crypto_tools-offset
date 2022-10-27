#!/usr/bin/python
from pickle import FALSE, TRUE
import sys

def sumPoints(p, q, mod, coeffs):
    res = [0,0]
    print(f"P({p}) + Q({q})")
    if p == q : 
        if p[1]==0:
            return res
        else:
            s = ((3*p[0]**2 + coeffs[0])) *pow((2 * p[1]),-1,mod)
    else:
        if p[0] == q[0]:
            return res
        else:
            s = (q[1] - p[1]) * pow((q[0] - p[0]),-1,mod)
    t = p[1] - s*p[0]
    print("s = ", s%mod)
    print("t = ", t%mod)
    res[0] = (s**2 - p[0] - q[0])%mod
    res[1] = (-s*res[0] - t)%mod
    print(f"=>  + {res}")
    return res

def checkGenaratorCandidate(gen_candidate, mod, coeffs):
    check = FALSE
    print(f"------------\n\nLet's try this generator candidate: {gen_candidate}") 
    point = gen_candidate
    i = 0
    while point != [0, 0]:        
        point = sumPoints(gen_candidate, point, mod, coeffs)
        print(f"------------\nP{i+2}: {point}"": ")
        i+=1
    
    if(i==len(findPoints(mod, coeffs))):
        print(f"Awesome, {gen_candidate} is a generator!")
        check = TRUE

    else:
        print("Too bad, {point} cardinal is only i={i}")

    return check

def findPoints(mod, coeffs):
    points_in_curve=[]
    for i in range(mod):
        for j in range(mod):
            if((j**2)%mod == (i**3 + coeffs[0]*i + coeffs[1])%mod):
                points_in_curve.append([i,j])
    return points_in_curve

def findGenerators(mod,coeffs):
    curve = findPoints(mod, coeffs)
    print(f"E: y^3 = x^2 + {coeffs[0]}.x + {coeffs[1]} over Z/{mod}Z ; \nPoints: {curve}")
    generators = []
    for point in curve: 
        if checkGenaratorCandidate(point, mod, coeffs):
            generators.append(point)
    return generators

def main(argv):
    try:
        if argv[0] == "--full":
            modulus = int(argv[1])
            coeffs=[int(argv[2]), int(argv[3])]
            print(findGenerators(modulus, coeffs))
        
        elif argv[0] == "--candidate":
            candidate=[int(argv[1]), int(argv[2])]
            coeffs=[int(argv[4]), int(argv[5])]
            modulus = int(argv[3])
            checkGenaratorCandidate(candidate, modulus, coeffs)

        elif argv[0] == "--sum":
            pointP=[int(argv[1]), int(argv[2])]
            pointQ=[int(argv[3]), int(argv[4])]
            modulus = int(argv[5])
            print(modulus)
            coeffs=[int(argv[6]), int(argv[7])]
            sumPoints(pointP, pointQ, modulus, coeffs)

        elif argv[0] == "-h":
            print("Find generators: --full <modulus> <a> <b>")
            print("CheckCandidate:  --candidate <x> <y> <modulus> <a> <b>")
            print("SumPoints:       --sum <xp> <yp> <xq> <yq>")
        
        else:
            print("Not recognized argument: choose between --full --candidate --sum or -h for help")

    except:
        print("Find generators: --full <modulus> <a> <b>")
        print("CheckCandidate:  --candidate <x> <y> <modulus> <a> <b>")
        print("SumPoints:       --sum <xp> <yp> <xq> <yq> <modulus> <a> <b>")

    return 0

if __name__ == "__main__":
   main(sys.argv[1:])
