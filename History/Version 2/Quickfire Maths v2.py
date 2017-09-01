from tkinter import *
from random import choice, randint

class windowSetup():
    def __init__(self):
        self.window = Tk()
        self.window.config()
        self.window.title("Quick Fire Maths")

        self.canvas = Canvas(self.window, width=600, height=600)  # Creating a canvas
        self.canvas.pack()

        ########## welcomeScreen() Objects ##########
        self.bImage = PhotoImage(file="welcome_screen.gif")  # Importing the image

        self.rFrame = Frame(self.window, bg="#7ad7ff")  # Making the frame in which the radio buttons and their label will reside
        self.cFrame = Frame(self.window, bg="#7ad7ff")  # Making the frame in which the check buttons and their label will reside

        self.modeVar = IntVar()  # Making the variable for the radio buttons
        self.addVar = IntVar()  # Making the variable for check buttons
        self.subVar = IntVar()
        self.multVar = IntVar()

        # Setting the default value of radio buttons
        self.modeVar.set(1)

        # Setting the default value of check buttons
        self.addVar.set(1)
        self.subVar.set(1)
        self.multVar.set(1)

        # Creating the radio buttons & label
        self.rLabel = Label(self.rFrame, bg="#7ad7ff", text="Please choose a mode", font="Courier 12 italic")
        self.roundButton = Radiobutton(self.rFrame, bg="#7ad7ff", text="Round Mode", font="Courier 10", variable=self.modeVar, value=1)
        self.unlimitedButton = Radiobutton(self.rFrame, bg="#7ad7ff", text="Unlimited Mode", font="Courier 10", variable=self.modeVar, value=2)

        # Creating the check buttons & label
        self.cLabel = Label(self.cFrame, bg="#7ad7ff", text="Please choose question types", font="Courier 12 italic")
        self.addButton = Checkbutton(self.cFrame, bg="#7ad7ff", text="Addition", font="Courier 10", variable=self.addVar)
        self.subButton = Checkbutton(self.cFrame, bg="#7ad7ff", text="Subtraction", font="Courier 10", variable=self.subVar)
        self.multButton = Checkbutton(self.cFrame, bg="#7ad7ff", text="Multiplication", font="Courier 10", variable=self.multVar)

        # Creating the start button
        self.startButton = Button(self.window,
                                  bg="#7ad7ff", relief=GROOVE,
                                  text="START", font="Courier 20",
                                  width=10,
                                  command=self.gameStart
                                  )

        # Packing the radio buttons & labels
        self.rLabel.pack(side=TOP)
        self.roundButton.pack(side=LEFT)
        self.unlimitedButton.pack(side=LEFT)

        # Packing the check buttons & labels
        self.cLabel.pack(side=TOP)
        self.addButton.pack(side=LEFT)
        self.subButton.pack(side=LEFT)
        self.multButton.pack(side=LEFT)

        ########## questionScreen() WIDGETS ##########
        self.inputBox = Entry(self.window, width=10, font="Courier 30")
        self.inputVar = IntVar()
        self.inputButton = Button(self.window,
                                  bg="#7ad7ff", relief=GROOVE,
                                  text="SUBMIT", font="Courier 20",
                                  width=10,
                                  command=lambda: self.inputVar.set(self.inputBox.get())
                                  )

        ########## answerScreen() WIDGETS ##########

        ########## finalScreen() WIDGETS ##########

    def gameStart(self):
        process = processes(self.canvas,
                            addition=self.addVar.get(),
                            subtraction=self.subVar.get(),
                            multiplication=self.multVar.get()
                            )
        if process.settingCheck():
            if self.modeVar.get() == 1:
                for x in range(10):
                    question=process.questionCaller()
                    self.questionScreen(question)
                    self.inputButton.wait_variable(self.inputVar)
                    self.answerScreen()

    def welcomeScreen(self):  # method to display the welcome screen
        self.canvas.delete("all")  # Clear the screen

        self.canvas.create_image(300, 300, image=self.bImage)  # Displaying the background image
        self.canvas.create_text(300, 50, text="Welcome to Quick Maths", font="Courier 30 italic", fill="#ff0000")

        self.canvas.create_window(300, 300, window=self.rFrame)  # Displaying the radio buttons
        self.canvas.create_window(300, 400, window=self.cFrame)  # Displaying the check buttons

        self.canvas.create_window(300, 500, window=self.startButton)  # Displaying the start button

    def questionScreen(self, question):
        self.canvas.delete("all")  # Clear the screen

        self.canvas.create_image(300, 300, image=self.bImage)  # Displaying the background image
        self.canvas.create_text(300, 50, text="Question <n>", font="Courier 30 italic", fill="#ff0000")

        self.canvas.create_text(300, 250, text=question, font="Courier 50 italic", fill="#00ff00")

        self.canvas.create_window(300, 400, window=self.inputBox)
        self.canvas.create_window(300, 500, window=self.inputButton)


    def answerScreen(self):
        """
        if self.process.inputCheck(self.canvas, self.inputBox):
            self.canvas.delete("all")
            self.process.answerCheck(self.inputBox)

            self.canvas.create_image(300, 300, image=self.bImage)
        """

    def finalScreen(self):
        pass

class processes():
    def __init__(self, canvas, **settings):
        self.canvas = canvas
        self.sList = [variable for variable in settings if settings[variable]==1]
        self.atLeastOnce = []

    def settingCheck(self):
        if len(self.sList) == 0:
            self.canvas.create_text(300, 440, fill="#ff0000",
                               text="You must choose at least one", font="Courier 15"
                               )
            return(0)
        return(1)

    def inputCheck(self, inputBox):
        try:
            int(inputBox.get())
        except:
            self.canvas.create_text(300, 360, text="Incorrect Input", font="Courier 15", fill="#ff0000")
            return(0)
        return(1)

    def answerCheck(self, inputBox):
        inputBox.get()
        pass

    def questionCaller(self):
        if len(self.atLeastOnce) != len(self.sList):  # Checking to see if there are any types that have not been asked
            while 1:
                nextQuestion = choice(self.sList)  # Randomly choosing a quesiton type
                if nextQuestion in self.atLeastOnce:  # Checking to see if question type has been asked
                    continue  # If yes, generate new question
                self.atLeastOnce.append(nextQuestion)  # If not, add the question type ot the list of asked questions
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

        return(self.question)

    def addCreator(self):
        self.question = "{}+{}".format(randint(10, 99), randint(2, 99))

    def subCreator(self):
        firstNumber = randint(10, 99)
        while 1:
            secondNumber = randint(5, 98)
            if secondNumber >= firstNumber:
                continue
            break
        self.question = "{}-{}".format(firstNumber, secondNumber)

    def multCreator(self):
        self.question = "{}*{}".format(randint(2, 9), randint(2, 9))

window1 = windowSetup()
window1.welcomeScreen()
window1.window.mainloop()