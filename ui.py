from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Courier"
DISTANCE = 300
HEIGHT = 250


class UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=20, background=THEME_COLOR)
        self.canvas = Canvas(width=DISTANCE, height=HEIGHT, bg="white", highlightthickness=0)
        self.quest = self.canvas.create_text(DISTANCE/2, HEIGHT/2, fill="black",
                                             font=(FONT_NAME, 20, "italic"), width=DISTANCE - 50)
        self.get_next_quest()
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        self.score_label = Label(
            font=(FONT_NAME, 15), text=f"Score:{self.quiz.score}",
            bg=THEME_COLOR, pady=10, fg="white")
        self.score_label.grid(row=0, column=1)
        right = PhotoImage(file="./images/true.png")
        self.good = Button(image=right, highlightthickness=0, border=0, command=self.right_button)
        self.good.grid(row=2, column=0)
        wrong = PhotoImage(file="./images/false.png")
        self.bad = Button(image=wrong, highlightthickness=0, border=0, command=self.wrong_button)
        self.bad.grid(row=2, column=1)
        self.window.mainloop()

    def get_next_quest(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(tagOrId=self.quest, text=q_text)

    def right_button(self):
        correct_answer = self.quiz.check_answer("True")
        self.plenty_config(answer_is_correct=correct_answer)

    def wrong_button(self):
        correct_answer = self.quiz.check_answer("False")
        self.plenty_config(answer_is_correct=correct_answer)

    def switch_white(self):
        self.canvas.config(bg="white")

    def close_window(self):
        self.window.destroy()

    def plenty_config(self, answer_is_correct):
        self.score_label.config(text=f"Score:{self.quiz.score}")
        if answer_is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, func=self.switch_white)
        if self.quiz.still_has_questions():
            self.get_next_quest()
        else:
            self.canvas.itemconfig(
                tagOrId=self.quest,
                text=f"Game Over! Your Score is {self.quiz.score}/{len(self.quiz.question_list)}"
            )
            self.window.after(3000, func=self.close_window)

