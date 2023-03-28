from tkinter import *
import tkinter as tk 

import PIL.Image
import PIL.ImageTk

import random

TotalBrickCount = 0
brickCounter = 0
BrickLayers = 0

CountToPizza = 0 
pizzaOvenCounter = 0

CountToHouse = 0
houseCounter = 0

CountToSam = 0
SamfordCounter = 0


def add_to_brickCounter():
    global brickCounter
    global BrickLayers
    global TotalBrickCount

    global CountToPizza
    global CountToHouse
    global CountToSam

    brickCounter +=1 * (1 + 2*BrickLayers)
    TotalBrickCount +=1 * (1 + 2*BrickLayers)

    CountToPizza +=1 * (1 + 2*BrickLayers)
    CountToHouse +=1 * (1 + 2*BrickLayers)
    CountToSam +=1 * (1 + 2*BrickLayers)

    if brickCounter == 1:
        textBrick.config(text= str(brickCounter) + "    Brick Clicked")
    else:
        textBrick.config(text= str(brickCounter) + "    Bricks Clicked")
    
    textTotal.config(text= "You've Clicked " + str(TotalBrickCount) + " Bricks!")

    if CountToPizza >= 100:
        CountToPizza = 0
        add_to_pizzaCounter()

    if CountToHouse == 50000:
        CountToHouse = 0
        add_to_houseCounter()
    if CountToSam == 3000000:
        CountToSam == 0
        add_to_samfordCounter()        
    
def add_to_pizzaCounter():
    global pizzaOvenCounter
    pizzaOvenCounter+=1
    if pizzaOvenCounter == 1:
        textPizza.config(text= str(pizzaOvenCounter) + "    Pizza Oven Assembled")
    else:
        textPizza.config(text= str(pizzaOvenCounter) + "    Pizza Ovens Assembled")

def add_to_houseCounter():
    global houseCounter
    houseCounter+=1
    if houseCounter == 1:
        textHouse.config(text= str(houseCounter ) + "    House Built")
    else:
        textHouse.config(text= str(houseCounter ) + "    Houses Built")

def add_to_samfordCounter():
    global SamfordCounter
    SamfordCounter+=1
    if SamfordCounter == 1:
        textSam.config(text= str(SamfordCounter) + "    Samford Hall Constructed")
    else:
        textSam.config(text= str(SamfordCounter) + "    Samford Halls Constructed")

def add_BrickLayer():
    global BrickLayers
    global brickCounter

    if brickCounter >= 50:
        BrickLayers+=1
        brickCounter-= 50

    if brickCounter == 1:
        textBrick.config(text= str(brickCounter) + "    Brick Clicked")
    else:
        textBrick.config(text= str(brickCounter) + "    Bricks Clicked")

    if BrickLayers == 1:
        BrickLayerCount.config(text= str(BrickLayers) + "    Brick Layer")
    else:
        BrickLayerCount.config(text= str(BrickLayers) + "    Brick Layers")



#Setup
root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height= 500)
canvas.grid(columnspan=25, rowspan=25)


root.iconbitmap("BrickICO.ico")
root.title('Brick Clicker')

#Creating Elements
#Bricks CLicked
textBrick = Label(root, text= str(brickCounter) + "   Bricks Clicked" )
#Pizza Ovens Built
textPizza = Label(root, text= str(pizzaOvenCounter) + "   Pizza Ovens Assembled" )
#Houses Built
textHouse = Label(root, text= str(houseCounter) + "   Houses Built" )
#Samford Halls Built
textSam = Label(root, text= str(SamfordCounter) + "   Samford Halls Constructed" )

#THE BRICK
IMG = PIL.Image.open("brickPNG.png")
brickIMG = PIL.ImageTk.PhotoImage(IMG)
BrickBtn = tk.Button(root,image=brickIMG,
                 command= add_to_brickCounter, borderwidth= 0)


#Logo
IMG = PIL.Image.open("Logo.png")
LogoIMG = PIL.ImageTk.PhotoImage(IMG)
LogoLabel = tk.Label(root,image=LogoIMG, borderwidth=0)

#Brick Layer Element
BuyBrickLayer = tk.Button(root,text='Buy 1 Brick Layer',
                 command= add_BrickLayer)
BrickLayerCount = Label(root, text= str(BrickLayers) + "   Brick Layers" )

BrickLayerInfo1 = Label(root, text= "**Buying Brick Layers Cost 50 Bricks Each, but can" )
BrickLayerInfo2 = Label(root, text= "  Exponentially Increase the Value of Each Brick Click**")

textTotal = Label(root, text= "You've Clicked " + str(TotalBrickCount) + " Bricks!"  )

#Formatting Elements
BrickBtn.grid(column=18, row=1)
LogoLabel.grid(column=1, row=1)
textTotal.grid(column=13, row=25)

BuyBrickLayer.grid(column= 1, row= 10)
BrickLayerCount.grid(column= 1, row=11)
BrickLayerInfo1.grid(column= 1, row= 16)
BrickLayerInfo2.grid(column=1, row=17)

textBrick.grid(column=20, row=11)
textPizza.grid(column=20, row= 13)
textHouse.grid(column=20, row=15)
textSam.grid(column=20, row= 17)






root.mainloop()


