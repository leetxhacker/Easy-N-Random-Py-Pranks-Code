import tkinter as tk

error = tk.Tk()
error.withdraw()

while True:
    tk.messagebox.showerror("Error", "Critical system!")
    tk.messagebox.showwarning("Warning", "Your computer has crashed!")
    tk.messagebox.showinfo("Info", "Please contact technical support!")
