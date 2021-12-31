import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random
t=None
words={}
canvasImg=None
canvas_text=None
canvasLabel=None
word={}
cards=None
def nextWord(canvas1):
    global word,cards
    global t
    cards.after_cancel(t)
    word=random.choices(words)
    canvas1.itemconfig(canvas_text,text=word[0]['French'],fill='black')
    canvas1.itemconfig(canvasImg,image=cardFront)
    canvas1.itemconfig(canvasLabel, text='French',fill='black')
    t = cards.after(3000,flipCard,canvas1)
    #words.remove(word[0])
    #print(len(words))
    pass
def flipCard(canvas1):
    canvas1.itemconfig(canvasImg,image=cardBack)
    canvas1.itemconfig(canvasLabel,text='English',fill='white')
    canvas1.itemconfig(canvas_text, text=word[0]['English'], fill='white')

def know(canvas1):
    global word,words
    words.remove(word[0])
    print(len(words))
    nextWord(canvas1)
def dontKnow(canvas1):
    nextWord(canvas1)

def loadCard(num):
    print(num[0])
    if num[0] == 0:
        fileName = "./flash-card-project-start/data/french_words.csv"
        file = pd.read_csv(fileName)
    global words
    words=file.to_dict(orient="records")
    global cards
    cards = tk.Toplevel()
    cards.title(langListBox.get(num))
    cards.config(padx=10, pady=10, bg=BACKGROUND_COLOR)
    canvas1 =tk.Canvas(cards, height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
    global canvasImg
    global canvas_text
    global canvasLabel
    canvasImg=canvas1.create_image(400, 263, image=cardFront)
    canvasLabel=canvas1.create_text(400, 150, text="French", font=("Arial", 30, "italic"))
    canvas_text=canvas1.create_text(400, 220, text="Card", font=("Arial", 40, "bold"))
    canvas1.grid(row=0, column=0,rowspan=3,columnspan=3)
    okButton=tk.Button(cards,image=rightButImg,highlightthickness=0,command=lambda:know(canvas1))
    okButton.grid(row=3,column=0)
    dontKnow=tk.Button(cards,image=wrongButImg,highlightthickness=0,command=lambda:nextWord(canvas1))
    dontKnow.grid(row=3,column=2)
    global t
    t = cards.after(3000,flipCard,canvas1)
    nextWord(canvas1)



def list_box_used():
    num = langListBox.curselection()
    loadCard(num)


langList = ["French to English"]
BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()
cardBack = tk.PhotoImage(file="./flash-card-project-start/images/card_back.png")
cardFront = tk.PhotoImage(file="./flash-card-project-start/images/card_front.png")
rightButImg = tk.PhotoImage(file="./flash-card-project-start/images/right.png")
wrongButImg = tk.PhotoImage(file="./flash-card-project-start/images/wrong.png")
window.title("Flash Card")
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)
# main Window
canvas = tk.Canvas(window, height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=cardBack)
canvas.create_text(400, 100, text="FLASH CARD", font=("Arial", 40, "bold"))
canvas.grid(row=0, column=1)
langListBox = tk.Listbox(window, height=5, selectmode="SINGLE", font=("Arial", 20, "bold"), bg=BACKGROUND_COLOR,
                         highlightthickness=0)
langListBox.grid(row=0, column=1, padx=10, pady=10)
for item in langList:
    langListBox.insert(langList.index(item), item)

submit = tk.Button(image=rightButImg, command=list_box_used)
submit.grid(row=2, column=1)

tk.mainloop()
