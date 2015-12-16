# wordfreqfp.py

import string
import itertools

def removepunc(s):
    return s.translate(s.maketrans("", "", string.punctuation))

def getwords(fname):
    with open(fname) as f:
        return removepunc(f.read().lower()).split()

def frequency(words):
    return map(lambda xy: (xy[0], len(list(xy[1]))),
               itertools.groupby(sorted(words)))
            
def main():
    print(frequency(getwords("moby.txt")))
    
main()
