from tkinter import *
from random import choice, randint

class windowSetup():
    def __init__(self):
        ########## General Stuff ##########
        self.window = Tk()
        self.window.config()
        self.window.title("Quick Fire Maths")

        self.canvas = Canvas(self.window, width=600, height=600)  # Creating a canvas
        self.canvas.pack()

        # Importing image for welcome screen, question screen, and final screen
        self.bImage = PhotoImage(file="welcome_screen.gif")

        self.quitButton = Button(self.window,
                                bg="#ff2222", relief=GROOVE,
                                text="Quit", font="Courier 15",
                                width=4,
                                command=self.window.destroy
                                )

        ########## welcomeScreen() Stuff ##########
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
        self.roundEntry = Entry(self.rFrame, width=2)
        self.rEntryLabel = Label(self.rFrame, text="No. Rounds:", font="Courier 8 italic", bg="#7ad7ff")
        self.roundButton = Radiobutton(self.rFrame, bg="#7ad7ff",
                                       text="Round Mode", font="Courier 10",
                                       variable=self.modeVar, value=1,
                                       command=lambda: self.roundEntry.config(state=NORMAL))

        self.unlimitedButton = Radiobutton(self.rFrame, bg="#7ad7ff",
                                           text="Unlimited Mode", font="Courier 10",
                                           variable=self.modeVar, value=2,
                                           command=lambda: self.roundEntry.config(state=DISABLED))

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
                                  command=None
                                  )

        # Packing the radio buttons & labels
        self.rLabel.grid(row=0, column=0, columnspan=3)
        self.roundButton.grid(row=1, column=0, columnspan=2, sticky=W)

        self.roundEntry.grid(row=2, column=1, padx=5, pady=7)
        self.rEntryLabel.grid(row=2, column=0)

        self.unlimitedButton.grid(row=1, column=2, padx=20)

        # Packing the check buttons & labels
        self.cLabel.grid(row=0, column=0, columnspan=3)
        self.addButton.grid(row=1, column=0)
        self.subButton.grid(row=1, column=1)
        self.multButton.grid(row=1, column=2)

        # Error Messages
        self.gameTypeError = Label(self.cFrame,
                                   text="You must choose at least one", font="Courier 15",
                                   foreground="#ff0000", bg="#7ad7ff"
                                   )
        self.roundEntryError = Label(self.rFrame,
                                     text="Must be an integer\nCannot be greater than 20", font="Courier 8",
                                     foreground="#ff0000", bg="#7ad7ff"
                                     )

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
        self.correctImage = PhotoImage(file="correct_screen.gif")
        self.falseImage = PhotoImage(file="false_screen.gif")

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
                                  command=None
                                  )

        ########## overlay() WIDGETS ##########

        self.welcomeScreen()

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

        self.canvas.create_window(300, 490, window=self.startButton)  # Displaying the start button
        self.canvas.create_window(560, 570, window=self.quitButton)

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
        self.canvas.create_window(300, 490, window=self.inputButton)  # Creating the button to move on

        self.canvas.create_window(560, 570, window=self.quitButton)


    def answerScreen(self, question, uInput, correct):
        """
        Need to create background images
        Must set command of nextButton
        """
        self.canvas.delete("all")  # Clear the screen

        colour=None

        if correct:
            self.canvas.create_image(300, 300, image=self.correctImage)  # Displaying correct image
            self.canvas.create_text(300, 50, text="You Were Right!", font="Courier 30 italic")
            colour = "#9effb0"
        else:
            self.canvas.create_image(300, 300, image=self.falseImage)  # Displaying incorrect image
            self.canvas.create_text(300, 50, text="You Were Wrong!", font="Courier 30 italic")
            colour = "#ff9ead"

        self.canvas.create_text(300, 250, text="Question: {}".format(question), font="Courier 30 italic")

        self.canvas.create_text(300, 350, text="Your Input: {}".format(uInput), font="Courier 30 italic")
        self.canvas.create_text(300, 400, text="Answer: {}".format(eval(question)), font="Courier 30 italic")

        self.nextButton.config(bg=colour)
        self.canvas.create_window(300, 490, window=self.nextButton)
        self.canvas.create_window(560, 570, window=self.quitButton)

    def finalScreen(self, score, totalQuestions):
        """
        Need to create background images
        Must set command of restartButton
        """
        self.canvas.delete("all")  # Clear the screen

        self.canvas.create_image(300, 300, image=self.bImage)  # Displaying correct image
        self.canvas.create_text(300, 50, text="Your Final Score", font="Courier 30 italic")

        self.canvas.create_text(300, 350, text="{}/{}".format(score, totalQuestions), font="Courier 70 italic", fill="#ff00aa")

        self.canvas.create_window(300, 490, window=self.restartButton)
        self.canvas.create_window(560, 570, window=self.quitButton)

    def overlay(self, event):
        pass

    def overlayRemove(self, event):
        print(1, event)

class processes(windowSetup):
    def __init__(self):
        windowSetup.__init__(self)

        self.startButton.config(command=self.gameStart)
        self.restartButton.config(command=self.welcomeScreen)

        self.welcomeScreen()

    def gameStart(self):
        self.canvas.bind("<Button-2>", self.overlay)
        self.canvas.bind("<ButtonRelease-2>", self.overlayRemove)
        self.score = 0
        if self.settingCheck():
            if self.modeVar.get() == 1:
                for n in range(1, int(self.roundEntry.get())+1):
                    self.windowSequence(n)
                self.finalScreen(self.score, int(self.roundEntry.get()))
            elif self.modeVar.get() == 2:
                questionNo = 0
                while 1:
                    questionNo += 1
                    self.windowSequence(questionNo)

    def windowSequence(self, questionNumber):
        self.inputBox.delete(0, "end")
        self.questionCaller()
        self.questionScreen(self.question, questionNumber)
        while 1:
            self.inputButton.wait_variable(self.inputVar)
            if self.inputCheck(self.inputVar.get()):
                break
            continue

        self.answerScreen(question=self.question,
                            uInput=self.inputVar.get(),
                            correct=self.answerCheck(question=self.question, input=self.inputVar.get())
                          )
        self.nextButton.wait_variable(self.nextVar)

    def settingCheck(self):
        validSetting = 1
        if self.modeVar.get() == 1:
            try:
                int(self.roundEntry.get())
            except:
                self.roundEntryError.grid(row=2, column=2)
                validSetting = 0
            else:
                if int(self.roundEntry.get()) > 20 or int(self.roundEntry.get()) == 0:
                    self.roundEntryError.grid(row=2, column=2)
                    validSetting = 0

        elif self.modeVar.get() == 2:
            if self.roundEntryError in self.rFrame.winfo_children():
                self.roundEntryError.grid_forget()


        self.settings = {"addition":self.addVar.get(), "subtraction":self.subVar.get(),
                         "multiplication":self.multVar.get()
                         }
        # Dictionary of enabled settings, set to 0 to denote that the question type has not been asked
        self.sDict = {variable: 0 for variable in self.settings if self.settings[variable]}

        if len(self.sDict) == 0:
            self.gameTypeError.grid(row=3, column=0, columnspan=3)
            validSetting = 0

        else:
            if self.gameTypeError in self.cFrame.winfo_children():
                self.gameTypeError.grid_forget()

        return(validSetting)

    def inputCheck(self, input):
        try:
            int(input)
        except:
            self.canvas.create_text(
                                    300, 360, text="Incorrect Input",
                                    font="Courier 15", fill="#ff0000"
                                    )
            return(0)
        if len(input) > 12:
            self.canvas.create_text(
                                    300, 435, text="Cannot be longer than 12 digits",
                                    font="Courier 15", fill="#ff0000"
                                    )
            return(0)
        return(1)

    def answerCheck(self, input, question):
        if eval(question) != eval(input):
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
