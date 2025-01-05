from tkinter import Tk
from tkinter import ttk
from functools import partial

import os
import json
import ctypes

NUM_ROW = 5
NUM_COL = 4
WINDOW_TITLE = "Calculator"
WINDOW_SIZE = "500x500"
LAYOUT_PATH = os.path.join(
  os.path.dirname(os.path.abspath(__file__)), 
  "layout.json"
)

class GUI():

  def __init__(self, backend: ctypes.CDLL) -> None:
    self.backend = backend 
    self.calculator = backend.getCalculator(None)
    self.toDisplay = ""
    self.fraction = False
    self.clearDisplay = False

    self.__setupWindow__()
    self.__setupFrame__()
    self.__placeLabel__()
    self.__placeButtons__()

  def run(self) -> None:
    self.window.mainloop()

  def __setupWindow__(self) -> None:
    self.window = Tk()
    self.window.title(WINDOW_TITLE)
    self.window.geometry(WINDOW_SIZE)
    self.window.resizable(False, False)

    for i in range(NUM_ROW):
      self.window.grid_rowconfigure(i, weight=1) 
    for i in range(NUM_COL):
      self.window.grid_columnconfigure(i, weight=1)

  def __setupFrame__(self) -> None:
    self.frame = ttk.Frame(self.window, padding="5 5 5 5")
    self.frame.grid(column=0, row=0)

  def __placeLabel__(self) -> None:
    self.label = ttk.Label(
      self.window,
      font=("Times 25"), 
      justify="right",
      anchor="center"
    )
    self.label.grid(
        row=0, 
        column=0, 
        columnspan=4,
        ipadx=15,
        ipady=25,
        sticky="e"
    )

  def __placeButtons__(self) -> None:
    layout = self.__loadLayout__()
    for i in range(NUM_ROW - 1): #1st row is for the label, so we subtract 1
      for j in range(NUM_COL):
        buttonData = layout[f"row{i + 1}"][f"button{j + 1}"]
        ttk.Button(
          self.window, 
          text=buttonData["display"], 
          command=partial(self.__handleButtons__, buttonData["action"]),
          ).grid(
            row=i + 1,
            column=j,
            ipadx=50,
            ipady=50,
          )

  def __loadLayout__(self) -> dict:
    with open(LAYOUT_PATH, 'r') as layoutFile:
      layout = json.load(layoutFile)
    return layout

  def __handleButtons__(self, input: str) -> None:
    if input.isnumeric(): self.__handleNumeric__(input)
    elif input == '.': self.__handleComma__()
    elif input == "=": self.__handleEqual__()
    else: self.__handleOperation__(input)

    self.label.config(text=self.toDisplay)

  def __handleNumeric__(self, input: str) -> None:
    if self.clearDisplay: 
      self.toDisplay = input
      self.clearDisplay = False
    elif self.toDisplay == "0":
      if input == "0": return
      else: self.toDisplay = input
    else: self.toDisplay += input

    self.backend.updateNumber(self.calculator, int(input))

  def __handleComma__(self) -> None:
    if self.clearDisplay:
      self.clearDisplay = False
      self.toDisplay = ""

    if not self.fraction: self.toDisplay += '.' #if the number is already a fraction, don't add the comma
    self.fraction = True
    
    if self.toDisplay == "" or not self.toDisplay[0].isnumeric():
      self.toDisplay = "0."

    self.backend.setFraction(self.calculator, True)

  def __handleEqual__(self) -> None:
    self.toDisplay = str(self.backend.calculate(self.calculator))
    self.clearDisplay = True

  def __handleOperation__(self, input: str) -> None:
    self.toDisplay = input
    self.fraction = False
    self.clearDisplay = True
    
    self.backend.setOperation(self.calculator, ord(input[0]))