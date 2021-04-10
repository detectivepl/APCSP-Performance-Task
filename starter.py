from tkinter import *
from PIL import ImageTk, Image

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

    koreanFlag = ImageTk.PhotoImage(Image.open("images\south-korean-flag.png").resize((300,200), Image.ANTIALIAS))
    kF = Label(canvas, image=koreanFlag)
    kF.image = koreanFlag
    kF.grid(row=2, column=0)
    koreanHello = Label(canvas, text="안녕하세요!", font="Times 32")
    koreanHello.grid(row=3, column=0)
    koreanButton = Button(canvas, text="Korean", font="Times 32", padx=100, command=lambda:[resetScreen(), langKor(), testScreen()])
    koreanButton.grid(row=4, column=0)

    spanishFlag = ImageTk.PhotoImage(Image.open("images\spanish-flag.png").resize((300,200), Image.ANTIALIAS))
    sF = Label(canvas, image=spanishFlag)
    sF.image = spanishFlag
    sF.grid(row=2, column=3)
    spanishHello = Label(canvas, text="¡Hola!", font="Times 32")
    spanishHello.grid(row=3, column=3)
    spanishButton = Button(canvas, text="Spanish", font="Times 32", padx=100, command=lambda:[resetScreen(), langSpan(), testScreen()])
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
    
    if langSwitch:
        lawlll = Label(canvas, text="yoyoyoyoyoyooyo")
        lawlll.grid(row=0, column=0)
    else:
        lawlll = Label(canvas, text="dsafsadfdsaf")
        lawlll.grid(row=0, column=0)
    
    car = ImageTk.PhotoImage(Image.open("images\car.png"))
    carr = Label(canvas, image=car)
    carr.image = car
    carr.grid(row=2, column=3)
    
    #CHANGE THIS 
    bton = Button(canvas, text="Goback", command=lambda:[resetScreen(), introScreen()])
    bton.grid(row=1,column=1)
    
def resetScreen():
    canvas.destroy()
    
#Groundwork
root = Tk()
root.title("Biliteracy Test")
introScreen()

root.mainloop()

#Images from:
#   pixabay.com (Clker-Free-Vector-Images, deMysticWay)
#   flaticon.com (Vectors Market, )








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