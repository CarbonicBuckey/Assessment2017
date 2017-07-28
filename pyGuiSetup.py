from tkinter import *
from string import *

"""
Kevin Kim
File to create grids and buttons assosiated with the grid.
"""

class canvasSetup(object):
    def __init__(self, window, width=600, height=600, colour="#ffffff"):
        self.window = window
        self.canvas = Canvas(self.window, width=width, heigh=height, bg=colour)
        self.canvas.pack()

        self.buttonList = []
        self.buttonLocList = []
        self.buttonWidthList = []

    def mouseClick(self, event):
        # Defining the coords
        x = event.x
        y = event.y

        # Going through all the possible buttons
        for n, button in enumerate(self.buttonList):
            xCoord = self.buttonLocList[n][0]  # Defining the top left x Coordinate of the box
            if x in range(xCoord, xCoord + self.buttonWidthList[n]):  # If within range of a box in the x axis
                yCoord = self.buttonLocList[n][1]  # Define the y axis corner
                if y in range(yCoord, yCoord + self.buttonWidthList[n]): # Check to see if within range of y axis
                    print(button)

class gridCaller(canvasSetup):
    def __init__(self, canvasSetup, row, column, firstX, firstY, distance=70, width=60, colour="#ffff00"):
        # Colour yellow by default

        # Defining variables for future use
        self.row = row  # Row, the y axis
        self.column = column  # Column, the x axis
        self.firstX = firstX  # Defining the X for the very top left corner of the first box
        self.firstY = firstY  # Defining the Y for the very top left corner of the first box
        self.distance = distance  # Distance between the first point of the first box, and the first point of the second box
        self.width = width  # Width and height of the box
        self.colour = colour
        self.canvasSetup = canvasSetup

        for y in range(row):  # Creating boxes in the first row first
            for x in range(column):  # Creating boxes in the columns per row
                canvasSetup.canvas.create_rectangle(
                                            firstX + distance * x,
                                            firstY + distance * y,

                                            (firstX + distance * x) + width,
                                            (firstY + distance * y) + width,

                                            fill=colour, outline="black"
                                            )

                canvasSetup.buttonLocList.append([firstX + distance * x, firstY + distance * y])
                canvasSetup.buttonWidthList.append(width)

    def gridText(self, textList=None, textOrder="calculator", font="Times 30 bold", colour="#000000", activeColour=None):
        if textList == None and textOrder=="calculator":  # If a list of text is not given, assume numbers
            textList = [x + (self.column * self.row - (self.column - 1)) - self.column * y for y in range(self.row)
                        for x in range(self.column)]
        elif textList == None and textOrder=="sequential":
            textList = [n for n in range(1, self.column*self.row+1)]

        elif textList == "alphabet":
            textList = [ascii_lowercase[n] for n in range(self.column*self.row)]

        for y in range(self.row):  # Basically the same logic as that seen in init
            for x in range(self.column):
                n = x + self.column * y  # finding the correct placement in the list
                self.canvasSetup.canvas.create_text(
                                                    (self.firstX + self.width / 2) + self.distance * x,  # x loc of text
                                                    (self.firstY + self.width / 2) + self.distance * y,  # y loc of text
                                                    text=textList[n],
                                                    font=font,
                                                    fill=colour,
                                                    activefill=activeColour
                                                    )
                self.canvasSetup.buttonList.append(textList[n])  # Adding created button labels to a list for loc determining

window = Tk()
canvas1 = canvasSetup(window, colour="#99ffff")
canvas2 = canvasSetup(window, colour="#0000ff")

canvas1.canvas.pack(side=LEFT)
canvas2.canvas.pack(side=RIGHT)

grid1 = gridCaller(canvas1, row=4, column=4, firstY=10, firstX=10, colour="#00ff00")
grid2 = gridCaller(canvas1, row=3, column=3, firstX=290, firstY=290, width=90, distance=100, colour="#ff0000")
grid3 = gridCaller(canvas1, row=4, column=4, firstX=290, firstY=10, colour="#ffffff")
grid4 = gridCaller(canvas2, row=1, column=5, firstX=10, firstY=10)
grid5 = gridCaller(canvas2, row=5, column=1, firstX=10, firstY=80)

grid1.gridText(activeColour="#ffffff", textOrder="sequential")
grid2.gridText(colour="#00ffff", font="comicsans 50 bold")
grid3.gridText(textList="alphabet", font="comicsans 30 italic")
grid4.gridText(textList="alphabet")
grid5.gridText(textList=[ascii_lowercase[n] for n in range(1, 6)])


canvas1.canvas.bind("<Button-1>", canvas1.mouseClick)
canvas2.canvas.bind("<Button-1>", canvas2.mouseClick)

mainloop()