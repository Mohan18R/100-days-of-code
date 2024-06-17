import tkinter as tk
from tkinter import messagebox
import time

# Sample text for typing test
sample_text = """Typing speed is an important skill that can be improved with practice. 
The average typing speed is around 40 words per minute, 
but with regular practice, you can achieve speeds of up to 100 words per minute."""


# Function to start the test
def start_test():
    global start_time
    start_time = time.time()
    typing_area.config(state='normal')
    typing_area.delete("1.0", tk.END)
    typing_area.focus()
    start_button.config(state='disabled')
    finish_button.config(state='normal')


# Function to finish the test and calculate WPM
def finish_test():
    end_time = time.time()
    typed_text = typing_area.get("1.0", tk.END).strip()
    typing_area.config(state='disabled')
    start_button.config(state='normal')
    finish_button.config(state='disabled')

    # Calculate correctly typed words
    correct_word_count = count_correct_words(sample_text, typed_text)

    # Calculate words per minute (WPM)
    elapsed_time = end_time - start_time
    wpm = correct_word_count / (elapsed_time / 60)

    # Display results
    messagebox.showinfo("Typing Test Result",
                        f"You typed {correct_word_count} correct words in {elapsed_time:.2f} seconds.\nYour typing speed is {wpm:.2f} words per minute.")
    typing_area.delete("1.0", tk.END)


# Function to count correctly typed words
def count_correct_words(reference_text, typed_text):
    reference_words = reference_text.split()
    typed_words = typed_text.split()
    correct_count = 0

    # Compare words
    for ref_word, typed_word in zip(reference_words, typed_words):
        if ref_word == typed_word:
            correct_count += 1

    return correct_count


# Create the main application window
root = tk.Tk()
root.title("Typing Speed Test")

# Instruction label
instruction_label = tk.Label(root, text="Type the following text as fast as you can and click 'Finish' when done:")
instruction_label.pack(pady=10)

# Display sample text
sample_text_label = tk.Label(root, text=sample_text, wraplength=500, justify="left")
sample_text_label.pack(pady=10)

# Text area for typing
typing_area = tk.Text(root, height=10, width=60, wrap="word", state='disabled')
typing_area.pack(pady=10)

# Start and Finish buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", command=start_test, bg="#4CAF50", fg="white",
                         font=("Helvetica", 14, "bold"), padx=20, pady=10)
start_button.pack(side="left", padx=10)

finish_button = tk.Button(button_frame, text="Finish", command=finish_test, state='disabled', bg="#F44336", fg="white",
                          font=("Helvetica", 14, "bold"), padx=20, pady=10)
finish_button.pack(side="left", padx=10)

# Run the Tkinter event loop
root.mainloop()
