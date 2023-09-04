import tkinter as tk
from tkinter import simpledialog, messagebox

def get_commit_message():
    while True:
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        # Set the width of the messagebox (double the default)
        root.geometry('400x100')

        message = simpledialog.askstring("Commit Message", "Enter your commit message:")
        
        if message and len(message) <= 50:
            return message
        elif not message:
            # Handle if the user closes the dialog or presses Cancel
            return None
        else:
            messagebox.showerror("Error", "Commit message exceeds 50 characters!")
            root.destroy()

commit_message = get_commit_message()

if commit_message:
    print(commit_message)
