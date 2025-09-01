from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Tkinter class")
icon = PhotoImage(file='Py_class/download.png')
window.iconphoto(True,icon)
window.config(background="cyan")
label = Label("Hello world")
window.mainloop()