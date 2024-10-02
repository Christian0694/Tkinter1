from tkinter import *

root = Tk() #crea el main window


#crea un label, igual que en windows forms
myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Segunda linea")
myLabel3 = Label(root, text="Tercera linea")

#myLabel.pack() #muestra en pantalla ajustado al label

#se llenan en los widgets en grids
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)
myLabel3.grid(row=2, column=1)



#crea un text box
e = Entry(root, width=50)
e.insert(0,"Enter your name here")
e.grid(row=4,column=0)




#funcion onclick
it = 1
itx = 5
ity = 0
def myClick():
    global it #declaramos como global variable
    nuevo_text = myLabel.cget("text") + str(it) + "|" #cget obtiene el texto del label
    myLabel.config(text=nuevo_text) #modificamos el texto del label
    it+=1

    global itx, ity
    myLabelx = Label(root, text="Hello" + e.get()) #agregamos un nuevo label al hacer click
    myLabelx.grid(row=itx, column=ity) #posicionamos
    itx+=1
    ity+=1



#crea un boton, igual que en windows forms
#padx y pady son el width y heigh del boton
myButton = Button(root, text="Click Me!", padx=50, pady=50, command=myClick, fg="red", bg="yellow")
myButton.grid(row=3, column=3)





root.mainloop() #event loop