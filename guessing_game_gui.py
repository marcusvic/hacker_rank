import tkinter as tk
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x200")

        self.selected_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(
            root, text="I'm thinking of a number between 1 and 100.")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Guess", command=self.check_guess)
        self.button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.restart_button = tk.Button(
            root, text="Play Again", command=self.restart_game)
        self.restart_button.pack(pady=5)
        self.restart_button.config(state=tk.DISABLED)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess > self.selected_number:
                self.result_label.config(text="Too high!")
            elif guess < self.selected_number:
                self.result_label.config(text="Too low!")
            else:
                self.result_label.config(
                    text=f"You got it in {self.attempts} guesses!")
                self.button.config(state=tk.DISABLED)
                self.restart_button.config(state=tk.NORMAL)
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def restart_game(self):
        self.selected_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)


# Create the GUI app
root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
