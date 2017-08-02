from tkinter import *

class windowSetup():
    def __init__(self):
        self.window = Tk()  # Defining window

        self.sideFrame = Frame()  # Defining side frame

        self.modeVar = IntVar()  # Defining the variable that will be changed by the radio buttons
        self.modeVar.set(0)  # Setting default value of mode to round

        self.addVar = IntVar()  # Defining the variable that will be changed by the check buttons
        self.subVar = IntVar()
        self.multVar = IntVar()

        # Creating the labels
        modeLabel = Label(self.sideFrame, text="Mode: ")
        questionLabel = Label(self.sideFrame, text="Question Type: ")

        # Creating the radio buttons
        roundRadio = Radiobutton(self.sideFrame, text="Round Mode", variable=self.modeVar, value=0)
        unlimitedRadio = Radiobutton(self.sideFrame, text="Unlimited Mode", variable=self.modeVar, value=1)

        # Creating the check buttons
        addCheck = Checkbutton(self.sideFrame, text="addition", variable=self.addVar)
        subCheck = Checkbutton(self.sideFrame, text="subtraction", variable=self.subVar)
        multCheck = Checkbutton(self.sideFrame, text="multiplication", variable=self.multVar)

        # Start buttons
        startButton = Button(self.sideFrame, text="Start", width=16, bg="#00ff00")

        # Creating the canvas
        self.canvas = Canvas(self.window, width=600, height=600, bg=None)

        # Packing everything
        modeLabel.pack(anchor=W)
        roundRadio.pack(anchor=W)
        unlimitedRadio.pack(anchor=W)

        questionLabel.pack(anchor=W)
        addCheck.pack(anchor=W)
        subCheck.pack(anchor=W)
        multCheck.pack(anchor=W)

        startButton.pack()

        self.sideFrame.pack(side=RIGHT)
        self.canvas.pack(side=LEFT)

    def welcome(self):
        self.canvas.config(bg="#aaddff")
        self.canvas.create_text(300, 150, text="Welcome to Quickfire Maths", font="Ascii 30 bold", fill="#0011dd")
        self.canvas.create_text(300, 400, text="θ", font="Ascii 200 italic", fill="#55aaff")

window1 = windowSetup()
window1.welcome()

window1.window.mainloop()