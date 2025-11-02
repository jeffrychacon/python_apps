import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import shutil
import os

# Target folder (you can make this dynamic too)
TARGET_FOLDER = "imported_files"

# Ensure the folder exists
os.makedirs(TARGET_FOLDER, exist_ok=True)

def import_files():
    # Ask user to select multiple files
    file_paths = filedialog.askopenfilenames(title="Select files to import")
    if not file_paths:
        return  # User cancelled

    # Copy each file into the target folder
    for path in file_paths:
        try:
            filename = os.path.basename(path)
            dest = os.path.join(TARGET_FOLDER, filename)
            shutil.copy(path, dest)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import {filename}:\n{e}")
            return

    messagebox.showinfo("Success", f"Imported {len(file_paths)} file(s) into '{TARGET_FOLDER}'")

# GUI setup
root = tk.Tk()
root.title("File Importer")

ttk.Button(root, text="Import Files", command=import_files).pack(pady=20)

root.mainloop()
