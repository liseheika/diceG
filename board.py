from dice import Dice 
import tkinter

class Board():
    def __init__(self):
        self.dice = list()

    def addDice(self):
        self.dice.append(Dice(6))

    def clear(self):
        self.dice.clear()