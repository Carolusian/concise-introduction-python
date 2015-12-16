# dna.py

from random import choice

def complement(dna):
    result = ""
    for c in dna:
        if c == "A":
            result += "T"
        elif c == "T":
            result += "A"
        elif c == "C":
            result += "G"
        elif c == "G":
            result += "C"
    return result

def reversecomp(dna):
    return complement(dna)[::-1]

def random_dna(length=30):
    fragment = ""
    for j in range(length):
        fragment += choice("ACGT")
    return fragment
        
def main():
    for i in range(10):
        dna = random_dna()
        print(dna + "   " + reversecomp(dna))
        print(complement(dna) + "\n")

main()
