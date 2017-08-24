from random import choice, randint

class processes():
    def __init__(self, canvas):
        """
        Requires input of the canvas, and a dictionary
        """
        self.canvas = canvas

    def settingCheck(self, **settings):
        self.sDict = {variable: 0 for variable in settings if settings[variable]}  # Dictionary of enabled settings

        print(self.sDict)
        if len(self.sDict) == 0:
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

    def answerCheck(self, inputBox, question):
        if eval(question) == int(inputBox.get()):
            return(0)
        return(1)

    def questionCaller(self):
        if 0 in self.sDict.values():
            nextQuestion = choice([key for key in self.sDict.key() if self.sDict[key]==0])
            self.sDict[nextQuestion] = 1
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