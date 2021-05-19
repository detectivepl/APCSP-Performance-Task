import random
from tkinter import *
from PIL import ImageTk, Image


sentenceListTXT = open("sentenceList.txt", "r")
sentenceList = sentenceListTXT.read().split("\n")
sentenceListTXT.close()

score = 0

def generateQuestion(difficulty):
    global question
    global answerBox
    global enterButton
    newCanvas()
    scoreCard = Label(canvas, text="Score: " + str(score), font="Times 12")
    scoreCard.grid(row=0, column=0)
    instructionCard = Label(canvas, text="Copy the sentence in the box above. Press 'Enter' to check your answer.")
    instructionCard.grid(row=3, column=1)
    answerBox = Entry(canvas, width=100, borderwidth=5)
    answerBox.grid(row=2, column=1)
    enterButton = Button(canvas, text="Enter", borderwidth=5, command=enterValue)
    enterButton.grid(row=2, column=2)
    if difficulty == "easy":
        for i in sentenceList:
            wordCount = i.count(" ") + 1
            if wordCount <= 10:
                question = i
                sentenceList.remove(i)
                break
    else:
        for i in sentenceList:
            wordCount = i.count(" ") + 1
            if wordCount > 10:
                question = i
                sentenceList.remove(i)
                break        
    entryText = Label(canvas, text=question, font="Times 16")
    entryText.grid(row=1, column=1)

def enterValue():
    ans = answerBox.get()
    resetScreen()
    if ans != question:
        displayScore()
    else:
        global score
        score += 1
        if score < 5:
            generateQuestion("easy")
        else:
            generateQuestion("hard")
        
def resetScreen():
    #This removes everything on the page
    canvas.destroy()
    
def displayScore():
    #This displays the user's score at the end of the game
    newCanvas()
    wrongX = ImageTk.PhotoImage(Image.open("wrong.png"))
    x1 = Label(canvas, image=wrongX)
    x2 = Label(canvas, image=wrongX)
    x1.image = wrongX
    x2.image = wrongX
    x1.grid(row=0, column=0)
    x2.grid(row=0, column=2)
    endMessage = Label(canvas, text="You made a typo!", font="Times 71")
    endMessage.grid(row=0, column=1)
    endScore = Label(canvas, text="Final score: " + str(score), font="Times 40")
    endScore.grid(row=1,column=1)
# 
# def correctMessage():
#     newCanvas()
# 
#     correct = Label(canvas, text="Nice", font="Times 20")
#     correct.grid(row=0, column=1)
#     print("WTSDFIOFJSif")
#     # resetScreen()

def newCanvas():
    #This creates a new canvas
    global canvas
    canvas = Canvas(root)
    canvas.grid(row=0, column=0)

def playGame():
    #This starts the game loop with an easy question
    generateQuestion("easy")


#PSVM
root = Tk()
root.title("Typing Test")
root.geometry("950x500")
root.grid_columnconfigure(10, minsize=100)
root.grid_rowconfigure(10, minsize=100)
playGame()
root.mainloop()
