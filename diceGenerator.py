import tkinter as tk
from config import *

class app():
    def __init__(self) -> None:
        pass

# Call constructor
window = tk.Tk()

# Configure window properties
window.geometry(WINSIZE)
window.title("Dice generator")

# Layout elements
welcomeLabel = tk.Label(window, text="Choose a die to start with", font=(FONT, FONTSIZE))
welcomeLabel.pack(padx=20, pady=20) 


# Frame
# a group you can put other elements into
frame = tk.Frame(window)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.columnconfigure(4, weight=1)
frame.columnconfigure(5, weight=1)

# Dice buttons
but4 = tk.Button(frame, text="4", font=(FONT, FONTSIZE))
but4.grid(row=0, column=0)
but6 = tk.Button(frame, text="6", font=(FONT, FONTSIZE))
but6.grid(row=0, column=1)
but8 = tk.Button(frame, text="8", font=(FONT, FONTSIZE))
but8.grid(row=0, column=2)
but10 = tk.Button(frame, text="10", font=(FONT, FONTSIZE))
but10.grid(row=0, column=3)
but12 = tk.Button(frame, text="12", font=(FONT, FONTSIZE))
but12.grid(row=0, column=4)
but20 = tk.Button(frame, text="20", font=(FONT, FONTSIZE))
but20.grid(row=0, column=5)

frame.pack()


# set main loop
window.mainloop()






