from tkinter import *

class windowSetup():
    def __init__(self):
        self.window = Tk()
        self.window.config()
        self.window.title("Quick Fire Maths")

        self.canvas = Canvas(self.window, width=600, height=600)  # Creating a canvas
        self.canvas.pack()

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
                                  command=None
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
        self.inputButton = Button(self.window,
                                  bg="#7ad7ff", relief=GROOVE,
                                  text="SUBMIT", font="Courier 20",
                                  width=10,
                                  command=None
                                  )

        ########## answerScreen() WIDGETS ##########
        self.nextButton = Button(self.window,
                                  bg="#7ad7ff", relief=GROOVE,
                                  text="Next Question", font="Courier 20",
                                  width=10,
                                  command=None
                                  )
        ########## finalScreen() WIDGETS ##########
        self.restartButton = Button(self.window,
                                  bg="#7ad7ff", relief=GROOVE,
                                  text="restart?", font="Courier 20",
                                  width=10,
                                  command=None
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

    def questionScreen(self, question):
        """
        Need to create background images
        Must set command of inputButton
        """
        self.canvas.delete("all")  # Clear the screen

        self.canvas.create_image(300, 300, image=self.bImage)  # Displaying the background image
        self.canvas.create_text(300, 50, text="Question <n>", font="Courier 30 italic", fill="#ff0000")

        self.canvas.create_text(300, 250, text=question, font="Courier 50 italic", fill="#00ff00")

        self.canvas.create_window(300, 400, window=self.inputBox)  # Creating the entry button
        self.canvas.create_window(300, 500, window=self.inputButton)  # Creating the button to move on


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

    def finalScreen(self, questionCorrect, totalQuestions):
        """
        Need to create background images
        Must set command of restartButton
        """
        self.canvas.delete("all")  # Clear the screen

        self.canvas.create_image(300, 300, image=self.bImage)  # Displaying correct image
        self.canvas.create_text(300, 50, text="Your Final Score", font="Courier 30 italic")

        self.canvas.create_text(300, 350, text="{}/{}".format(questionCorrect, totalQuestions), font="Courier 70 italic", fill="#ff00aa")

        self.canvas.create_window(300, 500, window=self.restartButton)

window1 = windowSetup()
window1.finalScreen(5, 10)
window1.window.mainloop()