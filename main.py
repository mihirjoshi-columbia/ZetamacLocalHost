import tkinter as tk
import random
import time

class ZetamacClone:
    def __init__(self, root):
        self.root = root
        self.root.title("Zetamac Clone")
        self.root.geometry("800x600")  # Make the GUI larger

        # Game Variables
        self.score = 0
        self.time_left = 60  # seconds
        self.current_question = ""
        self.answer = 0

        # UI Elements
        self.timer_label = tk.Label(root, text=f"Time Left: {self.time_left}s", font=("Arial", 20))
        self.timer_label.pack(pady=20)

        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 20))
        self.score_label.pack(pady=20)

        self.question_label = tk.Label(root, text="", font=("Arial", 30))
        self.question_label.pack(pady=40)

        self.answer_entry = tk.Entry(root, font=("Arial", 24), justify='center')
        self.answer_entry.pack(pady=20)
        self.answer_entry.bind("<Return>", self.check_answer)
        self.answer_entry.bind("<KeyRelease>", self.auto_check_answer)

        # Start Game
        self.generate_question()
        self.update_timer()

    def generate_question(self):
        operation = random.choice(["+", "-", "*", "/"])

        if operation == "+":
            num1 = random.randint(2, 100)
            num2 = random.randint(2, 100)
            self.answer = num1 + num2
        elif operation == "-":
            num1 = random.randint(2, 100)
            num2 = random.randint(2, 100)
            self.answer = num1 - num2
        elif operation == "*":
            num1 = random.randint(2, 30)
            num2 = random.randint(2, 100)
            self.answer = num1 * num2
        elif operation == "/":
            num2 = random.randint(2, 100)
            num1 = num2 * random.randint(2, 30)  # Ensure divisible
            self.answer = num1 // num2

        self.current_question = f"{num1} {operation} {num2}"
        self.question_label.config(text=self.current_question)

    def check_answer(self, event=None):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.answer:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.answer_entry.delete(0, tk.END)
                self.generate_question()
        except ValueError:
            pass  # Ignore invalid inputs

    def auto_check_answer(self, event):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.answer:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.answer_entry.delete(0, tk.END)
                self.generate_question()
        except ValueError:
            pass  # Ignore invalid inputs

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.question_label.config(text="Time's up!")
        self.answer_entry.config(state=tk.DISABLED)

# Run the Game
if __name__ == "__main__":
    root = tk.Tk()
    game = ZetamacClone(root)
    root.mainloop()

