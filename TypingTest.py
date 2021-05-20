from tkinter import *
from PIL import ImageTk, Image

sentenceListTXT = open("sentenceList.txt", "r")
sentenceList = sentenceListTXT.read().split("\n")
sentenceListTXT.close()

score = 0

def generateQuestion(difficulty):
    newCanvas()
    global question
    global answerBox
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
    entryText = Label(canvas, text=question, font="Times 16")
    entryText.grid(row=1, column=1)
    if noMoreHardWords:
        resetScreen()
        winScreen()

def enterValue():
    global ans
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

def findError(lastQuestion, lastAnswer):
    if len(lastQuestion) > len(lastAnswer):
        return 1
    elif len(lastQuestion) < len(lastAnswer):
        return 2
    return 3

def newCanvas():
    global canvas
    canvas = Canvas(root)
    canvas.grid(row=0, column=0)

def resetScreen():
    canvas.destroy()

def winScreen():
    newCanvas()
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

def loseScreen():
    newCanvas()
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

def startTest():
    generateQuestion("easy")


root = Tk()
root.title("Typing Test")
root.geometry("950x500")
root.grid_columnconfigure(10, minsize=100)
root.grid_rowconfigure(10, minsize=100)
startTest()
root.mainloop()
