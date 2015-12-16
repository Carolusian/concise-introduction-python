# wordfreq.py

import string

def getwords(fname):
    with open(fname) as f:
        s = f.read().lower()
    s = s.translate(s.maketrans("", "", string.punctuation))
    return s.split()

def frequency(words):
    d = {}
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def display(d):
    for key in sorted(d):
        print(key, d[key])
        
def main():
    words = getwords("moby.txt")
    display(frequency(words))
    
main()
