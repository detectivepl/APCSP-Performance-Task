#tkinter module by Fredrik Lundh
from tkinter import *
#PIL module created by Fredrik Lundh
from PIL import ImageTk, Image

#Gets list from file
sentenceListTXT = open("sentenceList.txt", "r")
sentenceList = sentenceListTXT.read().split("\n")
sentenceListTXT.close()

#User score
score = 0

#Generates a question window depending on difficulty
def generateQuestion(difficulty):
    newCanvas()
    global question
    global answerBox
    #Using tkinter module created by Fredrik Lundh
    scoreCard = Label(canvas, text="Score: " + str(score), font="Times 12")
    answerBox = Entry(canvas, width=100, borderwidth=5)
    enterButton = Button(canvas, text="Enter", borderwidth=5, command=enterValue)
    instructionCard = Label(canvas, text="Copy the sentence in the box above. Press 'Enter' to check your answer.")

    scoreCard.grid(row=0, column=0)
    answerBox.grid(row=2, column=1)
    enterButton.grid(row=2, column=2)
    instructionCard.grid(row=3, column=1)

    noMoreHardWords = False
    if difficulty == "easy":
        for i in sentenceList:
            wordCount = i.count(" ") + 1
            if wordCount <= 10:
                question = i
                sentenceList.remove(i)
                break
    else:
        noMoreHardWords = True
        for i in sentenceList:
            wordCount = i.count(" ") + 1
            if wordCount > 10:
                question = i
                sentenceList.remove(i)
                noMoreHardWords = False
                break
    #Using tkinter module created by Fredrik Lundh
    entryText = Label(canvas, text=question, font="Times 16")
    entryText.grid(row=1, column=1)
    if noMoreHardWords:
        resetScreen()
        winScreen()

#Registers the user inputted sentence after clicking enter
def enterValue():
    global ans
    #Using tkinter module created by Fredrik Lundh
    ans = answerBox.get()
    resetScreen()
    if ans != question:
        loseScreen()
    else:
        global score
        score += 1
        if score < 5:
            generateQuestion("easy")
        else:
            generateQuestion("hard")

#Finds the type of error the user made
def findError(lastQuestion, lastAnswer):
    if len(lastQuestion) > len(lastAnswer):
        return 1
    elif len(lastQuestion) < len(lastAnswer):
        return 2
    return 3

#Creates a new canvas
def newCanvas():
    global canvas
    #Using tkinter module created by Fredrik Lundh
    canvas = Canvas(root)
    canvas.grid(row=0, column=0)

#Destroys the current canvas
def resetScreen():
    #Using tkinter module created by Fredrik Lundh
    canvas.destroy()

#Displays the winner's screen
def winScreen():
    newCanvas()
    #Using PIL module created by Fredrik Lundh
    #Using tkinter module created by Fredrik Lundh
    rightV = ImageTk.PhotoImage(Image.open("right.png"))
    v1 = Label(canvas, image=rightV)
    v2 = Label(canvas, image=rightV)
    v1.image = rightV
    v2.image = rightV
    v1.grid(row=0, column=0)
    v2.grid(row=0, column=2)
    winMessage = Label(canvas, text="Nice Job!", font="Times 40")
    endScore = Label(canvas, text="All correct", font="Times 20")
    winMessage.grid(row=0, column=1)
    endScore.grid(row=1, column=1)

#Displays the loser's screen, the user's final score, and the user's error
def loseScreen():
    newCanvas()
    #Using PIL module created by Fredrik Lundh
    #Using tkinter module created by Fredrik Lundh
    wrongX = ImageTk.PhotoImage(Image.open("wrong.png"))
    x1 = Label(canvas, image=wrongX)
    x2 = Label(canvas, image=wrongX)
    x1.image = wrongX
    x2.image = wrongX
    x1.grid(row=0, column=0)
    x2.grid(row=0, column=2)

    box = LabelFrame(canvas, padx=55, pady=20)
    box.grid(row=1, column=1)

    errorCode = findError(question, ans)
    if errorCode == 1:
        errorTypeMessage = "You wrote too little!"
    elif errorCode == 2:
        errorTypeMessage = "You wrote too much!"
    else:
        errorTypeMessage = "You made a typo!"
        
    #Using tkinter module created by Fredrik Lundh
    endMessage = Label(canvas, text=errorTypeMessage, font="Times 40")
    lastq = Label(box, text="Sentence: ", font="Times 16")
    lastQuestion = Label(box, text=question, font="Times 16")
    lasta = Label(box, text="Your answer: ", font="Times 16")
    lastAnswer = Label(box, text=ans, font="Times 16")
    endScore = Label(canvas, text="Final score: " + str(score), font="Times 20")

    endMessage.grid(row=0, column=1)
    lastq.grid(row=1, column=0)
    lastQuestion.grid(row=1, column=1)
    lasta.grid(row=2, column=0)
    lastAnswer.grid(row=2, column=1)
    endScore.grid(row=3, column=1)

#Starts the test with an easy question
def startTest():
    generateQuestion("easy")


#Main
#Setting up the code to run
#Using tkinter module created by Fredrik Lundh
root = Tk()
root.title("Typing Test")
root.geometry("950x500")
root.grid_columnconfigure(10, minsize=100)
root.grid_rowconfigure(10, minsize=100)
startTest()
root.mainloop()
