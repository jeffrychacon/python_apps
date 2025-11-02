import tkinter
from tkinter import Entry

def button_clicked():
    #my_label.config(text="Button Clicked!")
    my_label.config(text=input.get())

window = tkinter.Tk()
window.title("My First GUI Application")
window.minsize(width=500, height=300)
window.config(padx=20, pady=200)

#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="Another New Text")
#my_label.pack()
my_label.grid(column=0, row=0)  

#Button
#button = tkinter.Button(text="Click Me", command=lambda: my_label.config(text="Button Clicked!"))
button = tkinter.Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

button2 = tkinter.Button(text="New Button")
button2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
#input.pack()
input.grid(column=3, row=2)











window.mainloop()