"""
Created on Mon Mar 24 17:12:47 2025

after self.root.configure
self.root.resizable(False, False)

@author: sharr, torr, er
"""

import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator Simulator")
        self.root.geometry("700x500")
        self.root.configure(bg="pink")

        tk.Label(root, text="Welcome to Password Generator Simulator!", font=("Times New Roman", 16, "bold"), bg="lightblue").pack(pady=20)

        tk.Label(root, text="Enter desired password length (between 10 and 30)", font=("Times New Roman", 16), bg="lightblue").pack(pady=10)
        self.length = tk.Entry(root, width=16, font=("Times New Roman", 16))
        self.length.pack()

        self.numbers = tk.BooleanVar()
        self.special = tk.BooleanVar()
        self.uppercase = tk.BooleanVar()

        tk.Checkbutton(root, text="Include Numbers", variable=self.numbers, font=("Times New Roman", 14), bg="lightblue").pack(pady=8)
        tk.Checkbutton(root, text="Include Special Characters", variable=self.special, font=("Times New Roman", 14), bg="lightblue").pack(pady=8)
        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.uppercase, font=("Times New Roman", 14), bg="lightblue").pack(pady=8)

        tk.Button(root, text="Generate Password", command=self.gen_pass, font=("Times New Roman", 16), bg="lightblue").pack(pady=10)

        self.passwordNum = tk.StringVar()
        tk.Entry(root, textvariable=self.passwordNum, font=("Times New Roman", 14), width=30, state="readonly").pack()

    def gen_pass(self):
        try:
            length = int(self.length.get())
            if length < 10 or length > 30:
                messagebox.showerror("Error", "Your length is invalid. It must be between 10-30")
                return

            if not ((self.numbers.get() and self.special.get()) or (self.numbers.get() and self.uppercase.get()) or (self.uppercase.get() and self.special.get())):
                messagebox.showerror("Error", "Please select at least two preference options.")
                return

            # Define required characters
            required_chars = list(random.choices(string.ascii_lowercase, k=2))  # At least 2 lowercase letters

            if self.numbers.get():
                required_chars += random.choices(string.digits, k=2)  # At least 2 numbers
            if self.special.get():
                required_chars += random.choices(string.punctuation, k=2)  # At least 2 special characters
            if self.uppercase.get():
                required_chars += random.choices(string.ascii_uppercase, k=2)  # At least 2 uppercase letters

            # Fill the rest of the password randomly
            all_characters = string.ascii_lowercase
            if self.numbers.get():
                all_characters += string.digits
            if self.special.get():
                all_characters += string.punctuation
            if self.uppercase.get():
                all_characters += string.ascii_uppercase

            remaining_length = length - len(required_chars)
            if remaining_length > 0:
                required_chars += random.choices(all_characters, k=remaining_length)

            random.shuffle(required_chars)  # Shuffle to mix characters
            password = ''.join(required_chars)
            self.passwordNum.set(password)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
