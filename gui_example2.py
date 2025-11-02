import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")  #title of the window
window.minsize(width=500, height=300) #minimum size
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold")) #create a label
my_label.pack(side="left")                  #place the label on the window



window.mainloop()  #keep the window open