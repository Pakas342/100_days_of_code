import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=300, height=100)


def miles_to_km():
    user_miles = miles.get()
    km = round(float(user_miles) * 1.60934, 2)
    kilometers.config(text=km)


miles_label = tkinter.Label(text="miles", font=("Arial", 12, "bold"))
miles_label.grid(row=1, column=3)
my_label = tkinter.Label(text="Is equal to", font=("Arial", 12, "bold"))
my_label.grid(row=2, column=0)
kilometers = tkinter.Label(text="", font=("Arial", 12, "bold"), justify=tkinter.CENTER)
kilometers.grid(row=2, column=1)
kilometers_label = tkinter.Label(text="kilometers", font=("Arial", 12, "bold"))
kilometers_label.grid(row=2, column=3)


miles = tkinter.Entry(justify=tkinter.CENTER)
miles.grid(row=1, column=1)
submit_button = tkinter.Button(text="Convert", command=miles_to_km)
submit_button.grid(row=3, column=1)



window.mainloop()