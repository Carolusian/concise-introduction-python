# dice.py

from random import randint

class Die:
    def __init__(self):
        self.roll()

    def roll(self):
        self.value = randint(1, 6)
    
    def __str__(self):
        return str(self.value)
    
    def __int__(self):
        return self.value
    
class Dice:
    def __init__(self, n=3):
        self.dice = [Die() for i in range(n)]
        
    def rollall(self):
        for die in self.dice:
            die.roll()
            
    def values(self):
        return list(map(int, self.dice))
    
    def count(self, value):
        return self.values().count(value)
    
    def __str__(self):
        return str(self.values())
    
def main():
    # Test
    dice = Dice(5)
    print("Initial:", dice)
    dice.rollall()
    print("After roll:", dice)
    print("Number of 2's:", dice.count(2))

if __name__ == "__main__":
    main()
