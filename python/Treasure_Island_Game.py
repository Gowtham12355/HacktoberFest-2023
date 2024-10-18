import tkinter as tk
from tkinter import messagebox

# Create the main game class
class TreasureIslandGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Treasure Island Game")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to Treasure Island. Your mission is to find the treasure!", font=("Arial", 14), wraplength=400)
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start Game", font=("Arial", 12), command=self.start_game)
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Reset Game", font=("Arial", 12), command=self.reset_game, state=tk.DISABLED)
        self.reset_button.pack(pady=10)

    def start_game(self):
        self.start_button.config(state=tk.DISABLED)
        self.choice1()

    def reset_game(self):
        self.label.config(text="Welcome to Treasure Island. Your mission is to find the treasure!")
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

    def choice1(self):
        self.label.config(text="You're at a crossroad. Where do you want to go? Left or Right?")
        self.choice_frame = tk.Frame(self.root)
        self.choice_frame.pack(pady=10)

        left_button = tk.Button(self.choice_frame, text="Left", font=("Arial", 12), command=self.choice2)
        left_button.grid(row=0, column=0, padx=10)

        right_button = tk.Button(self.choice_frame, text="Right", font=("Arial", 12), command=self.game_over_hole)
        right_button.grid(row=0, column=1, padx=10)

    def choice2(self):
        self.choice_frame.pack_forget()
        self.label.config(text="You've come to a lake. Will you wait for a boat or swim across?")
        self.choice_frame = tk.Frame(self.root)
        self.choice_frame.pack(pady=10)

        wait_button = tk.Button(self.choice_frame, text="Wait", font=("Arial", 12), command=self.choice3)
        wait_button.grid(row=0, column=0, padx=10)

        swim_button = tk.Button(self.choice_frame, text="Swim", font=("Arial", 12), command=self.game_over_trout)
        swim_button.grid(row=0, column=1, padx=10)

    def choice3(self):
        self.choice_frame.pack_forget()
        self.label.config(text="You arrive at the island unharmed. There is a house with 3 doors: Red, Yellow, and Blue.")
        self.choice_frame = tk.Frame(self.root)
        self.choice_frame.pack(pady=10)

        red_button = tk.Button(self.choice_frame, text="Red", font=("Arial", 12), command=self.game_over_fire)
        red_button.grid(row=0, column=0, padx=10)

        yellow_button = tk.Button(self.choice_frame, text="Yellow", font=("Arial", 12), command=self.win_game)
        yellow_button.grid(row=0, column=1, padx=10)

        blue_button = tk.Button(self.choice_frame, text="Blue", font=("Arial", 12), command=self.game_over_beasts)
        blue_button.grid(row=0, column=2, padx=10)

    def game_over_hole(self):
        self.end_game("You fell into a hole. Game Over!")

    def game_over_trout(self):
        self.end_game("You were attacked by a giant trout. Game Over!")

    def game_over_fire(self):
        self.end_game("It's a room full of fire. Game Over!")

    def game_over_beasts(self):
        self.end_game("You entered a room of beasts. Game Over!")

    def win_game(self):
        self.end_game("Congratulations! You found the treasure and won the game!")

    def end_game(self, message):
        self.choice_frame.pack_forget()
        messagebox.showinfo("Game Over", message)
        self.reset_button.config(state=tk.NORMAL)


# Main game loop
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    game = TreasureIslandGame(root)
    root.mainloop()
