import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}")

root = tk.Tk()
root.title("User Info Form")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Use ttk for labels and entries
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background="#f0f0f0", foreground="#000000")
style.configure("TEntry", fieldbackground="#ffffff", foreground="#000000")

ttk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)
email_entry = ttk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

# Use tk.Button for visibility
submit_btn = tk.Button(root, text="Submit", command=submit_form, bg="#4CAF50", fg="#ffffff")
submit_btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
