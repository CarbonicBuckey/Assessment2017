from tkinter import *
from random import choice, randint

class windowSetup():
    def __init__(self):
        self.window = Tk()
        self.window.config()
        self.window.title("Quick Fire Maths")

        self.canvas = Canvas(self.window, width=600, height=600)  # Creating a canvas
        self.canvas.pack()

        self.quitButton = Button(self.window,
                                bg="#ff0000", relief=GROOVE,
                                text="Quit", font="Courier 20",
                                width=10,
                                command=sys.exit
                                )

        ########## welcomeScreen() Stuff ##########
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
        self.inputVar = StringVar()
        self.inputBox = Entry(self.window, width=10, font="Courier 30")
        self.inputButton = Button(self.window,
                                  bg="#7ad7ff", relief=GROOVE,
                                  text="SUBMIT", font="Courier 20",
                                  width=10,
                                  command=lambda: self.inputVar.set(self.inputBox.get())
                                  )

        ########## answerScreen() WIDGETS ##########
        self.nextVar = IntVar()
        self.nextButton = Button(self.window,
                                  bg="#7ad7ff", relief=GROOVE,
                                  text="Next", font="Courier 20",
                                  width=10,
                                  command=lambda: self.nextVar.set(1)
                                  )
        ########## finalScreen() WIDGETS ##########
        self.restartButton = Button(self.window,
                                  bg="#7ad7ff", relief=GROOVE,
                                  text="restart?", font="Courier 20",
                                  width=10,
                                  command=self.welcomeScreen
                                  )

    def welcomeScreen(self):  # method to display the welcome screen
        """
        Need to create background images
        Must set command of startButton
        """
        self.canvas.delete("all")  # Clear the screen

        self.canvas.create_image(300, 300, image=self.bImage)  # Displaying the background image
        self.canvas.create_text(300, 50, text="Welcome to Quick Maths", font="Courier 30 italic", fill="#ff0000")

        self.canvas.create_window(300, 300, window=self.rFrame)  # Displaying the radio buttons
        self.canvas.create_window(300, 400, window=self.cFrame)  # Displaying the check buttons

        self.canvas.create_window(300, 500, window=self.startButton)  # Displaying the start button
        self.canvas.create_window(500, 550, window=self.quitButton)

    def questionScreen(self, question, questionNo):
        """
        Need to create background images
        Must set command of inputButton
        """
        self.canvas.delete("all")  # Clear the screen

        self.canvas.create_image(300, 300, image=self.bImage)  # Displaying the background image
        self.canvas.create_text(300, 50, text="Question {}".format(questionNo), font="Courier 30 italic", fill="#ff0000")

        self.canvas.create_text(300, 250, text=question, font="Courier 50 italic", fill="#00ff00")

        self.canvas.create_window(300, 400, window=self.inputBox)  # Creating the entry button
        self.canvas.create_window(300, 500, window=self.inputButton)  # Creating the button to move on

        self.canvas.create_window(500, 550, window=self.quitButton)


    def answerScreen(self, question, uInput, correct):
        """
        Need to create background images
        Must set command of nextButton
        """
        self.canvas.delete("all")  # Clear the screen

        if correct:
            self.canvas.create_image(300, 300, image=self.bImage)  # Displaying correct image
            self.canvas.create_text(300, 50, text="You Were Right!", font="Courier 30 italic")
        else:
            self.canvas.create_image(300, 300, image=self.bImage)  # Displaying incorrect image
            self.canvas.create_text(300, 50, text="You Were Wrong!", font="Courier 30 italic")

        self.canvas.create_text(300, 250, text="Question: {}".format(question), font="Courier 30 italic")

        self.canvas.create_text(300, 400, text="Your Input: {}".format(uInput), font="Courier 30 italic")
        self.canvas.create_text(300, 450, text="Answer: {}".format(eval(question)), font="Courier 30 italic")

        self.canvas.create_window(300, 500, window=self.nextButton)
        self.canvas.create_window(500, 550, window=self.quitButton)

    def finalScreen(self, score, totalQuestions):
        """
        Need to create background images
        Must set command of restartButton
        """
        self.canvas.delete("all")  # Clear the screen

        self.canvas.create_image(300, 300, image=self.bImage)  # Displaying correct image
        self.canvas.create_text(300, 50, text="Your Final Score", font="Courier 30 italic")

        self.canvas.create_text(300, 350, text="{}/{}".format(score, totalQuestions), font="Courier 70 italic", fill="#ff00aa")

        self.canvas.create_window(300, 500, window=self.restartButton)
        self.canvas.create_window(500, 550, window=self.quitButton)

class processes(windowSetup):
    def __init__(self):
        windowSetup.__init__(self)
        self.welcomeScreen()

        self.totalQuestion = 0
        self.score = 0

    def gameStart(self):
        if self.settingCheck():
            if self.modeVar.get() == 1:
                self.totalQuestion = 10
                for n in range(1, self.totalQuestion+1):
                    self.windowSequence(n)
                self.finalScreen(self.score, self.totalQuestion)
            elif self.modeVar.get() == 0:
                self.totalQuestion = 0
                while 1:
                    self.totalQuestion += 1
                    self.windowSequence(self.totalQuestion)

    def windowSequence(self, questionNumber):
        self.inputBox.delete(0, "end")
        question=self.questionCaller()
        self.questionScreen(question, questionNumber)
        while 1:
            self.inputButton.wait_variable(self.inputVar)
            if self.inputCheck(self.inputVar.get()):
                break
            continue

        self.answerScreen(question=question,
                            uInput=self.inputVar.get(),
                            correct=self.answerCheck(question=question, input=self.inputVar.get())
                          )
        self.nextButton.wait_variable(self.nextVar)

    def settingCheck(self):
        self.setting = {"addition":self.addVar.get(), "subtraction":self.subVar.get(), "multiplication":self.multVar.get()}

        # Dictionary of enabled settings
        self.sDict = {variable: 0 for variable in self.setting if self.setting[variable]}

        print(self.sDict)
        if len(self.sDict) == 0:
            self.canvas.create_text(
                                    300, 440, fill="#ff0000",
                                    text="You must choose at least one", font="Courier 15"
                                    )
            return(0)
        return(1)

    def inputCheck(self, input):
        try:
            int(input)
        except:
            self.canvas.create_text(
                                    300, 360, text="Incorrect Input",
                                    font="Courier 15", fill="#ff0000"
                                    )
            return(0)
        return(1)

    def answerCheck(self, input, question):
        if eval(question) != int(input):
            return(0)
        self.score += 1
        return(1)

    def questionCaller(self):
        if 0 in self.sDict.values():
            nextQuestion = choice([key for key in self.sDict.keys() if self.sDict[key]==0])
            self.sDict[nextQuestion] = 1
        else:
            nextQuestion = choice([key for key in self.sDict.keys()])  # If all the questions were asked at least once generate random question

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

start = processes()
start.window.mainloop()
