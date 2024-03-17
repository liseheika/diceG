import tkinter as tk
import random


class Dice():
    def __init__(self, sides):
        self.value = 1
        self.sides = sides

    def roll(self):
        self.value = random.randint(1, self.sides)



