from tkinter import *
root=Tk() 
root.title("Dictionary") 
root.geometry("500x500")

label_of_mutable = Label(root)
label_of_immutable = Label(root)
label_of_tkinter = Label(root)

Dictionary = {'Mutable': 'Values can be changed just like a List',
              'Immutable': 'Values can not be changed just like a tuple',
              'Tkinter': 'It is the GUI library of python'
              }

def mutable():
  label_of_mutable["text"] = Dictionary['Mutable'] 

def immutable():
  label_of_immutable["text"] = Dictionary['Immutable'] 

def tkinter():
  label_of_tkinter["text"] = Dictionary['Tkinter'] 

button_tkinter = Button(root, text = "tkinter",command = tkinter)
button_tkinter.place(relx=0.5,rely=0.6,anchor = CENTER)  

button_immutable = Button(root, text = "immutable",command = immutable)
button_immutable.place(relx=0.5,rely=0.4,anchor = CENTER) 

button_mutable = Button(root, text = "mutable",command = mutable)
button_mutable.place(relx=0.5,rely=0.2,anchor = CENTER)

label_of_mutable.place(relx=0.5,rely=0.3,anchor = CENTER)

label_of_immutable.place(relx=0.5,rely=0.5,anchor = CENTER)

label_of_tkinter.place(relx=0.5,rely=0.7,anchor = CENTER)

      
root.mainloop()