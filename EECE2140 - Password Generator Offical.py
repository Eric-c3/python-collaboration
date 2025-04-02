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
        self.root.configure (bg= "pink")
        
        tk.Label(root, text="Welcome to Password Generator Simulator!", font=("Times New Roman", 16, "bold"), bg="lightblue").pack(pady=20)
        
        tk.Label(root, text="Enter desired password length (between 10 and 30)", font=("Times New Roman", 16), bg="lightblue").pack(pady=10)
        self.length = tk.Entry(root, width=16, font=("Times New Roman", 16))
        self.length.pack()
        
        self.numbers = tk.BooleanVar()
        self.special = tk.BooleanVar()
        self.uppercase = tk.BooleanVar()
        """self.lowercase = tk.BooleanVar()"""
        
        # foreground fg = "" will change the color of the text 
        tk.Checkbutton(root, text="Include Numbers", variable=self.numbers, font=("Times New Roman", 14), bg="lightblue").pack(pady=8)
        tk.Checkbutton(root, text="Include Special Characters", variable=self.special, font=("Times New Roman", 14), bg="lightblue").pack(pady=8)
        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.uppercase, font=("Times New Roman", 14), bg="lightblue").pack(pady=8)
        """tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.lowercase, font=("Times New Roman", 14), bg="lightblue").pack(pady=8)"""
        
        tk.Button(root, text="Generate Password", command=self.gen_pass, font=("Times New Roman", 16), bg="lightblue").pack(pady=10)
        
        self.passwordNum = tk.StringVar()
        tk.Entry(root, textvariable=self.passwordNum, font=("Times New Roman", 14), width=30, state="readonly").pack() # The read-only is so that the user cannot write in the text box
# However, because it is there and not state="normal" or no state at all, you cannot edit the background         
    def gen_pass(self):
        try:
            length = int(self.length.get())
            if length < 10 or length > 30:
                messagebox.showerror("Error", "Your length is invalid. It must be between 10-30")
                return
            
            if not ((self.numbers.get() and self.special.get()) or (self.numbers.get() and self.uppercase.get()) or (self.uppercase.get() and self.special.get())):
                messagebox.showerror("Error", "Please select at least two preference option.")
                return
            
            
            # This was the og
            """if not (self.numbers.get() or self.special.get() or self.uppercase.get()):
                messagebox.showerror("Error", "Please select at least one preference option.")
                return"""
                
            characters = string.ascii_lowercase
            if self.numbers.get():
                characters += string.digits
            if self.special.get():
                characters += string.punctuation
            if self.uppercase.get():
                characters += string.ascii_uppercase
                
            """if self.lowercase.get():
                characters += string.ascii_lowercase"""
                
            """
            NO MATTER what there will be letters 
            if we want only digits add the letters we must add more parameters
            
            
            ADD: MUSTS PICK TWO PARAMETERS
            
            
            
            """ 
            
            password = ''.join(random.choice(characters) for i in range(length))
            self.passwordNum.set(password)
            random.shuffle (password)
            
        except ValueError:
            messagebox.showerror("Error" , "Please enter a valid number.")
        
root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
