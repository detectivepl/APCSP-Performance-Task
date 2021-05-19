from tkinter import *
from PIL import ImageTk, Image
from numpy import random

# global questions
# questions = ["car", "dog", "cat", "chair", "book", "paper"]
# questions = ["car", "dog"]
# kAnswers = ["차", "개", "고양이", "의자", "책", "종이"]
kAnswers = ["차", "개"]
# sAnswers = ["carro", "perro", "gato", "silla", "libro", "papel"]
sAnswers = ["carro", "perro"]

def introScreen():
    global canvas
    canvas = Canvas(root)
    canvas.grid(row=0, column=0)
    top = Label(canvas, text="")
    top.grid(row=0, column=0, columnspan=3)
    entryText = Label(canvas, text="Biliteracy Test", font="Times 64")
    entryText.grid(row=0, column=1)
    entryDesc = Label(canvas, text="Test your language skills here!", font="Times 16")
    entryDesc.grid(row=1, column=1)
    #Korean
    koreanFlag = ImageTk.PhotoImage(Image.open("images\south-korean-flag.png").resize((300,200), Image.ANTIALIAS))
    kF = Label(canvas, image=koreanFlag)
    kF.image = koreanFlag
    kF.grid(row=2, column=0)
    koreanHello = Label(canvas, text="안녕하세요!", font="Times 32")
    koreanHello.grid(row=3, column=0)
    koreanButton = Button(canvas, text="Korean", font="Times 32", padx=100, borderwidth=5, command=lambda:[resetScreen(), langKor(), testScreen()])
    koreanButton.grid(row=4, column=0)
    #Spanish
    spanishFlag = ImageTk.PhotoImage(Image.open("images\spanish-flag.png").resize((300,200), Image.ANTIALIAS))
    sF = Label(canvas, image=spanishFlag)
    sF.image = spanishFlag
    sF.grid(row=2, column=3)
    spanishHello = Label(canvas, text="¡Hola!", font="Times 32")
    spanishHello.grid(row=3, column=3)
    spanishButton = Button(canvas, text="Spanish", font="Times 32", padx=100, borderwidth=5, command=lambda:[resetScreen(), langSpan(), testScreen()])
    spanishButton.grid(row=4, column=3)
    
def langKor():
    global langSwitch
    langSwitch = True
    
def langSpan():
    global langSwitch
    langSwitch = False
    
def testScreen():
    global canvas
    canvas = Canvas(root)
    canvas.grid(row=0, column=0)
    top = Label(canvas, text="")
    top.grid(row=0, column=0, columnspan=3)
    #Back Button
    backButton = Button(canvas, text="Go back", borderwidth=5, command=lambda:[resetScreen(), introScreen()])
    # backButton.grid(row=0,column=0)
    
    questions = ["car", "dog"]
    qImgs = []
    for i in questions:
        tempImg = ImageTk.PhotoImage(Image.open("images\\" + i + ".png"))
        tI = Label(canvas, image=tempImg)
        tI.image = tempImg
        qImgs.append(tI)
    
    # print(qImgs)
    
    while len(questions)>0:
        randVal = random.randint(len(questions))
        # print(randVal)
        if langSwitch:
            imgName = Label(canvas, text=questions[randVal])
            imgName.grid(row=0, column=1)
            qImgs[randVal].grid(row=1, column=1)
            questions.pop(randVal)
            qImgs.pop(randVal)
        else:
            imgName = Label(canvas, text="dsafsadfdsaf")
            imgName.grid(row=0, column=1)
    
    
    # qImgs[0].grid(row=1, column=1)
    answerBox = Entry(canvas, width=30, borderwidth=5)
    answerBox.grid(row=2, column=1)
    # enterButton = Button(canvas, text="Enter", borderwidth=5, command)
    

    
def resetScreen():
    canvas.destroy()
    
#Groundwork
root = Tk()
root.title("Biliteracy Test")
introScreen()

root.mainloop()

#Images from:
#   pixabay.com (Clker-Free-Vector-Images, deMysticWay)
#   flaticon.com (Vectors Market, Freepik, )








#   SCRAP CODE
#######################################################################
# e = Entry(root, width=50)
# e.pack()
# e.get()
# 
# 
# def myClick():
#     if e.get() == "Peter":
#         myLabel = Label(root, text="Sup")
#     else:
#         myLabel = Label(root, text="Lawl")
#     # myLabel = Label(root, text=e.get())
#     myLabel.pack()
# 
# myButton = Button(root, text="Enter your name", command=myClick, fg="blue", bg="red")
# myButton.pack()



# window = tk.Tk()
# 
# window.title("Python Tkinter Text Box")
# window.minsize(1000,1000)
# 
# def clickMe():
#     label.configure(text= 'Hello ' + name.get())
# 
# label = ttk.Label(window, text = "Enter Your Name")
# label.grid(column = 0, row = 0)
# 
# 
# 
# 
# name = tk.StringVar()
# nameEntered = ttk.Entry(window, width = 15, textvariable = name)
# nameEntered.grid(column = 0, row = 1)
# 
# 
# button = ttk.Button(window, text = "Click Me", command = clickMe)
# button.grid(column= 0, row = 2)
# 
# window.mainloop()