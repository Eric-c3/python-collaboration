"""
@author: sharr, torr, er
"""
import tkinter as tk
from tkinter import messagebox
import random
import string
import os

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
        
        # State of the download button is disabled since the password hasn't been created yet and the user has nothing to download.
        self.download_button = tk.Button(root, text="Download Password", command=self.download_password, font=("Times New Roman", 16), bg="lightblue", state="disabled")
        self.download_button.pack(pady=10)

        self.password = ""

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
            self.password = ''.join(required_chars)
            # Password is now generated and joined together with the required parameters created by us and user. 

            self.download_button.config(state="normal") # Enable download button since the password is now generated. 

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def download_password(self):
        if self.password:
            # Get the users downloads folder and name it password.txt (making it a text file)
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "password.txt")

            # Write the password to the file in downloads
            with open(downloads_path, "w") as file: # w means writing mode so we can rewrite anything in the current file (if the file was created before use)
                # Filling in the file we just created with the password that was just randomly generated 
                file.write(self.password)

            messagebox.showinfo("Success", f"Your password has been saved to:\n{downloads_path}")

root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
