# chuckgui.py

from dicegui import DiceGUI
from tkinter import *

class ChuckALuckGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.geometry("500x300")
        parent.title("Chuck-A-Luck")
        self.dice = DiceGUI(3, self)
        self.dice.pack(fill="y", expand=True)
        self.score = 0
        self.makecontrols()
        self.makescore()
        self.pack(fill="y", expand=True)
        
    def makecontrols(self):
        self.choice = IntVar()
        controlframe = Frame(self)
        for i in range(1, 7):
            Radiobutton(controlframe, text=str(i), value=i,
                        variable=self.choice).pack(side="left")
        Label(controlframe, width=5).pack(side="left")
        Button(controlframe, width=10, text="Roll",
               command=self.roll).pack(side="left")
        controlframe.pack()

    def makescore(self):
        self.scorestr = StringVar()
        Label(self, textvariable=self.scorestr,
              font=("Helvetica", 24)).pack(fill="y", expand=True)
        self.updatescore()
        
    def roll(self):
        self.dice.rollall()
        matches = self.dice.count(self.choice.get())
        self.score += matches if matches > 0 else -1
        self.updatescore()
        
    def updatescore(self):
        self.scorestr.set("Score: " + str(self.score))

root = Tk()
app = ChuckALuckGUI(root)
root.mainloop()
