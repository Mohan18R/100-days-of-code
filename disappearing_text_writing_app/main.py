import tkinter as tk
from tkinter import messagebox
import time
from threading import Timer

# Global variables
text_content = ""
last_input_time = time.time()
timeout_duration = 5  # Time in seconds
timer = None

def update_text(event=None):
    global text_content, last_input_time
    text_content = text_box.get("1.0", tk.END).strip()
    last_input_time = time.time()  # Update the last input time
    reset_timer()  # Reset and start the timer

def reset_timer():
    global timer
    if timer:
        timer.cancel()  # Cancel any existing timer
    timer = Timer(timeout_duration, check_inactivity)
    timer.start()

def check_inactivity():
    global text_content, last_input_time
    current_time = time.time()
    if current_time - last_input_time >= timeout_duration:
        clear_text()
    else:
        reset_timer()  # Restart the timer if still typing

def clear_text():
    global text_content
    text_box.delete("1.0", tk.END)
    text_content = ""
    messagebox.showinfo("Timeout", "You stopped typing! All text has been deleted.")

# Set up Tkinter window
root = tk.Tk()
root.title("Disappearing Writing App")
root.geometry("600x600")

# Create text box
text_box = tk.Text(root, font=("Arial", 14), wrap='word')
text_box.pack(expand=True, fill='both')

# Bind key release to update_text function
text_box.bind("<KeyRelease>", update_text)

# Start the application
root.mainloop()
