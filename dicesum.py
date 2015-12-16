# dicesum.py

from random import randint

class Die:
    def __init__(self):
        self.roll()
    
    def roll(self):
        self.value = randint(1, 6)
        
    def __str__(self):
        return str(self.value)

def main():
    rolls = int(input("Enter the number of times to roll: "))
    die1 = Die()
    die2 = Die()
    counts = [0] * 13
    for i in range(rolls):
        die1.roll()
        die2.roll()
        counts[die1.value + die2.value] += 1
    for i in range(2, 13):
        print(str(i) + ": " + str(counts[i]))
    
main()
