import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length should be a positive integer")
        
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        password_label.config(text="Generated Password: " + password)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Label and entry field for password length
length_frame = tk.Frame(root)
length_frame.pack()
length_label = tk.Label(length_frame, text="Password Length:")
length_label.pack(side="left")
entry_length = tk.Entry(length_frame)
entry_length.pack(side="left")

# Button to trigger password generation
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

# Label to display generated password
password_label = tk.Label(root, text="")
password_label.pack(pady=5)

# Start GUI main loop
root.mainloop()
