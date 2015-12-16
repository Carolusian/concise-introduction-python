# chuck.py

from dice import Dice

class ChuckALuck:
    def __init__(self):
        self.dice = Dice(3)
        self.score = 0
        
    def play(self):
        choice = int(input("Choose a number (0 to stop): "))
        while choice != 0:
            self.dice.rollall()
            print("The roll:", self.dice)
            matches = self.dice.count(choice)
            self.score += matches if matches > 0 else -1
            print("Current score:", self.score)
            choice = int(input("Choose a number (0 to stop): "))
        print("Thanks for playing.")
        
def main():
    game = ChuckALuck()
    game.play()

if __name__ == "__main__":
    main()
