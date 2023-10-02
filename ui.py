from quiz_brain import QuizBrain
from tkinter import *
from tkinter import messagebox

THEME_COLOR = "#375362"
FONT = ("ariel", 15, "italic")


class QuizzInterface:

    def __init__(self, quizz_brain: QuizBrain):
        self.quizz_brain = quizz_brain
        self.window = Tk()
        self.window.title = "Quizz Game"
        self.window.config(padx=50, pady=50, background=THEME_COLOR)

        self.score_text = Label(text="score: 0", fg="white", bg=THEME_COLOR, font=("ariel", 12))
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question here", font=FONT,
                                                     fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, borderwidth=0,
                                  command=self.user_ans_true)
        self.true_button.grid(row=2, column=0)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, borderwidth=0,
                                   command=self.user_ans_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_text.config(text=f"score: {self.quizz_brain.score}")
        if self.quizz_brain.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quizz_brain.next_question())
        else:
            self.final_score()

    def user_ans_true(self):
        self.give_feedback(self.quizz_brain.check_answer(user_answer="True"))

    def user_ans_false(self):
        self.give_feedback(self.quizz_brain.check_answer(user_answer="False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, func=self.get_next_question)

    def final_score(self):
        messagebox.showinfo(title="you ended the quiz!", message=f"Your results were: "
                                                                 f"{self.quizz_brain.score}/{self.quizz_brain.question_number}")
        self.canvas.itemconfig(self.question_text, text="You ended the quizzler!")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
