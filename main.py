from tkinter import *

root = Tk() #crea el main window

myLabel = Label(root, text="Hello World!") #crea un label, igual que en windows forms
myLabel2 = Label(root, text="Segunda linea")
myLabel3 = Label(root, text="Segunda linea")

#myLabel.pack() #muestra en pantalla ajustado al label


myLabel.grid(row=0, column=1)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=0, column=1)





root.mainloop() #event loop