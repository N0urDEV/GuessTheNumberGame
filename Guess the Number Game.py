from tkinter import *
import random

secret = random.randint(1, 100)

def check_guess():
    try:
        guess = int(number.get())
        if guess == secret:
            result.config(text="Congratulations! You guessed it!", fg="green")
        elif guess < secret:
            result.config(text="Try a higher number.", fg="orange")
        else:
            result.config(text="Try a lower number.", fg="orange")
    except ValueError:
        result.config(text="Please enter a valid number.", fg="red")

window = Tk()
window.title("Guess the Number")
window.geometry("300x200") 

Label(window, text="Guess the number (1-100):", font=("Arial", 12)).pack(pady=10)
number = Entry(window, font=("Arial", 12))
number.pack(pady=10)
Button(window, text="Check Guess", command=check_guess, font=("Arial", 12)).pack(pady=10)
result = Label(window, text="", font=("Arial", 12), fg="black")
result.pack(pady=10)

window.mainloop()
