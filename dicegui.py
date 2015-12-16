# dicegui.py

from dice import Dice
from tkinter import *

class DiceGUI(Frame, Dice):
    def __init__(self, n, parent):
        Frame.__init__(self, parent)
        Dice.__init__(self, n)
        self.loadimages()
        self.n = n
        self.labels = [Label(self) for i in range(self.n)]
        for i in range(self.n):
            self.setimage(i)
            self.labels[i].pack(side="left")
    
    def loadimages(self):
        self.images = [None] * 7
        for i in range(1, 7):
            fname = "die" + str(i) + ".ppm"
            self.images[i] = PhotoImage(file=fname)
            
    def rollall(self):
        Dice.rollall(self)
        for i in range(self.n):
            self.setimage(i)
            
    def setimage(self, i):
        self.labels[i].config(image=self.images[int(self.dice[i])])
