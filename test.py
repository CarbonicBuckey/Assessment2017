from tkinter import *

class initialise():
    def __init__(self, windowName=None):
        self.window = Tk()
        self.window.title(windowName)

    def gameStart(self):
        print(self.modeVar.get())

    def sideMenu(self):
        sideFrame = Frame(self.window)

        modeLabel = Label(sideFrame, text="What mode would you like?")
        self.modeVar = IntVar()

        modeButton1 = Radiobutton(sideFrame, text="Unlimited", variable=self.modeVar, value=1)
        modeButton2 = Radiobutton(sideFrame, text="RoundBased", variable=self.modeVar, value=2)

        startButton = Button(text="Start", command=self.gameStart)
        startButton.pack()

        modeLabel.pack()
        modeButton1.pack(anchor=W, side=BOTTOM)
        modeButton2.pack(anchor=W)

        sideFrame.pack()

window = initialise("Quickfire Maths")
window.sideMenu()

window.window.mainloop()

"""
class windowSetup():
    def __init__(self, window, width=500, height=500, colour="#00aaff"):
        self.canvas = Canvas(window, width=width, height=height, bg=colour)
        self.canvas.pack()

    def startUp(self):
        self.canvas.delete()

        self.canvas.create_text(250, 100, text="Welcome To Quickfire Math", font="Avenir 25 bold", fill="#ffff00")

        self.canvas.create_text(250, 250, text="θ", font="Avenir 120 italic", fill="#3333ff")

        self.canvas.create_rectangle(75, 400, 425, 450, fill="#ffff00")
        self.canvas.create_text(250, 425, text="Click to Play!", font="Avenir 20")

        self.canvas.bind("<>")

    def modeSelect(self):
        self.canvas.delete()
"""