import tkinter as tk
import random
import time

class ZetamacClone:
    def __init__(self, root):
        self.root = root
        self.root.title("Zetamac Clone")

        # Game Variables
        self.score = 0
        self.time_left = 60  # seconds
        self.current_question = ""
        self.answer = 0

        # UI Elements
        self.timer_label = tk.Label(root, text=f"Time Left: {self.time_left}s", font=("Arial", 16))
        self.timer_label.pack(pady=10)

        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 16))
        self.score_label.pack(pady=10)

        self.question_label = tk.Label(root, text="", font=("Arial", 24))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Arial", 18), justify='center')
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=self.check_answer)
        self.submit_button.pack(pady=10)

        # Start Game
        self.generate_question()
        self.update_timer()

    def generate_question(self):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        operation = random.choice(["+", "-", "*"])

        if operation == "+":
            self.answer = num1 + num2
        elif operation == "-":
            self.answer = num1 - num2
        elif operation == "*":
            self.answer = num1 * num2

        self.current_question = f"{num1} {operation} {num2}"
        self.question_label.config(text=self.current_question)

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.answer:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
        except ValueError:
            pass  # Ignore invalid inputs

        self.answer_entry.delete(0, tk.END)
        self.generate_question()

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
        self.submit_button.config(state=tk.DISABLED)

# Run the Game
if __name__ == "__main__":
    root = tk.Tk()
    game = ZetamacClone(root)
    root.mainloop()

