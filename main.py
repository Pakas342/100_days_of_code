from tkinter import *
from brain import Brain
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- Functions SETUP ------------------------------- #

brain = Brain()
word_to_know = brain.random_word()


def turn_around(language):
    if language == "French":
        canvas.itemconfig(canvas_image, image=front_card_img)
        canvas.itemconfig(language_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=f"{word_to_know['French']}", fill="black")
    elif language == "English":
        canvas.itemconfig(canvas_image, image=back_card_img)
        canvas.itemconfig(language_text, text="English", fill="white")
        canvas.itemconfig(word_text, text=f"{word_to_know['English']}", fill="white")


def success():
    if brain.not_all_know():
        global word_to_know, timer
        brain.right_answer(word_to_know)
        word_to_know = brain.random_word()
        turn_around("French")
        window.after_cancel(timer)
        timer = window.after(3000, func=turn_english)
    else:
        messagebox.showinfo(title="all words known", message="You know all words, congratulations!!!")


def wrong():
    global word_to_know, timer
    word_to_know = brain.random_word()
    turn_around("French")
    timer = window.after(3000, func=turn_english)


def turn_english():
    turn_around("English")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Card Info")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card_img)
language_text = canvas.create_text(400, 150, text="French", fill="black", font=("ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text=f"{word_to_know['French']}", fill="black", font=("ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=success)
right_button.grid(row= 1, column=0)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=wrong)
wrong_button.grid(row=1, column=1)

timer = window.after(3000, func=turn_english)

window.mainloop()
