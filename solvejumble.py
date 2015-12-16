# solvejumble.py

def signature(word):
    chars = list(word)
    chars.sort()
    return chars

def wordlist(fname):
    with open(fname) as f:
        return f.read().split()
    
def matches(jumble):
    sign = signature(jumble)
    result = []
    for word in wordlist("dictionary.txt"):
        if signature(word) == sign:
            result.append(word)
    return result

def main():
    jumble = input("Enter a scrambled word: ")
    print("Matches are:", matches(jumble))
    
main()
