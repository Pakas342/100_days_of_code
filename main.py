import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# Create a label

my_label = tkinter.Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.pack()





window.mainloop()