from tkinter import *
from random import choice, randint

class windowSetup():
    def __init__(self):
        self.window = Tk()
        self.welcomeScreen()

    def welcomeScreen(self):
        self.radioFrame = Frame(self.window)  # Creating frame to house radio buttons
        self.checkFrame = Frame(self.window)  # Creting frame ot house check buttons

        modeLabel = Label(self.radioFrame, text="Please choose your mode", font="Ascii 20 bold")
        typeLabel = Label(self.checkFrame, text="Please choose the types of questions", font="Ascii 20 bold")

        modeLabel.pack(anchor=W)
        typeLabel.pack(anchor=W)

        self.settingButtons = buttonSetup()
        self.settingButtons.radioButton(self.radioFrame, 1, LEFT, W, 'Round Mode', 'Unlimited')
        self.settingButtons.checkButton(self.checkFrame, LEFT, W, addition=1, subtraction=1, multiplication=1)

        self.radioFrame.grid(row=0, column=0, sticky=W, pady=10)
        self.checkFrame.grid(row=1, column=0, sticky=W, pady=10)

        startButton = Button(text="Start", font="Ascii 20 bold", command=self.start, width=20)
        startButton.grid(row=2, column=0)

    def questionScreen(self, question):
        canvas1 = Canvas(height=300, width=300)
        questionLabel = Label(text=question, font="ascii 50 bold")
        answerInput = Entry(width=20)

        questionWindow = canvas1.create_window(150, 100, window=questionLabel)
        inputWindow = canvas1.create_window(100, 200, window=answerInput)

        canvas1.pack()

    def clear(self):
        for objects in self.window.winfo_children():
            objects.destroy()

    def start(self):
        setting = self.settingButtons.results()

        if 1 not in setting[1].values():
            try:
                self.errorLabel.pack()

            except:
                self.errorLabel = Label(self.checkFrame, text="You must choose at least one", foreground="#ff0000")
                self.errorLabel.pack()

        else:
            question = questionSetup(setting[1])

            if setting[0] == 1:
                for n in range(10):
                    print(question.questionDecider())
                    self.clear()
                    self.questionScreen(question)


            elif setting[0] == 2:
                while 1:
                    question.questionDecider()
                    self.clear()
                    self.questionScreen(question)

class questionSetup():
    def __init__(self, setting):
        # Adding variables to list if they have value of 1
        self.sList = [variable for variable in setting if setting[variable]]
        self.atLeastOne = []  # List to make sure that all question types are asked at least once

    def questionDecider(self):
        if len(self.atLeastOne) != len(self.sList):  # Checking to see if there are any types that have not been asked
            while 1:
                nextQuestion = choice(self.sList) # Randomly choosing a quesiton type
                if nextQuestion in self.atLeastOne:  # Checking to see if question type has been asked
                    continue  # If yes, generate new question
                self.atLeastOne.append(nextQuestion) # If not, add the question type ot the list of asked questions
                break  # Stop generating questions

        else:
            nextQuestion = choice(self.sList)  # If all the questions were asked at least once generate random question

        # Calling appropriate functions
        if nextQuestion == "addition":
            self.addCreator()
        elif nextQuestion == "subtraction":
            self.subCreator()
        elif nextQuestion == "multiplication":
            self.multCreator()


    def addCreator(self):
        self.question = "{} + {}".format(randint(10, 99), randint(2, 99))

    def subCreator(self):
        firstNumber = randint(10, 99)
        while 1:
            secondNumber = randint(5, 98)
            if secondNumber >= firstNumber:
                continue
            break
        self.question = "{} - {}".format(firstNumber, secondNumber)

    def multCreator(self):
        self.question = "{} * {}".format(randint(1, 9), randint(1, 9))

    def __str__(self):
        return(self.question)

class buttonSetup():
    def radioButton(self, window, default=0, side=None, anchor=E, *varList):
        self.rButtonDict = {}
        self.rVar = IntVar()
        self.rVar.set(default)

        for n, variable in enumerate(varList):
            self.rButtonDict[variable] = Radiobutton(window, text=variable, variable=self.rVar, value=n+1)
            self.rButtonDict[variable].pack(side=side, anchor=anchor)

    def checkButton(self, window, side=None, anchor=E, **varList):
        self.varList = varList
        self.cButtonDict = {}
        self.cButtonDictVar = {}

        for variable in varList:
            self.cButtonDictVar[variable] = IntVar()
            self.cButtonDictVar[variable].set(varList[variable])
            self.cButtonDict[variable] = Checkbutton(window, text=variable, variable=self.cButtonDictVar[variable])
            self.cButtonDict[variable].pack(side=side, anchor=anchor)

    def results(self):
        mResults = self.rVar.get()
        cResults = {}

        for variable in self.varList:
            cResults[variable] = self.cButtonDictVar[variable].get()

        return(mResults, cResults)


windowSetup().window.mainloop()
