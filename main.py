import tkinter as tk
from tkinter import ttk, messagebox
from transformers import pipeline

# Initialize the Hugging Face QA pipeline
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

# Function to process question and provide an answer
def get_answer():
    context = context_text.get("1.0", tk.END).strip()  # Get context text from the GUI
    question = question_entry.get().strip()           # Get the question text from the GUI

    # Validate inputs
    if not context:
        messagebox.showerror("Error", "Please provide Context.")
        return
    if not question:
        messagebox.showerror("Error", "Please enter a Question.")
        return

    # Generate the answer using Hugging Face pipeline
    try:
        answer = qa_pipeline(question=question, context=context)
        answer_label.config(text=f"Answer: {answer['answer']}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main GUI window
root = tk.Tk()
root.title("Question Answering System")
root.geometry("600x500")
root.resizable(False, False)

# Create a style for a cleaner GUI
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TText", font=("Arial", 12))

# Title Label
title_label = ttk.Label(root, text="Question Answering System Using Hugging Face", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Context Text Area
context_label = ttk.Label(root, text="Context:")
context_label.pack(anchor="w", padx=10, pady=5)

context_text = tk.Text(root, height=10, width=70, wrap=tk.WORD)
context_text.pack(padx=10, pady=5)

# Question Input
question_label = ttk.Label(root, text="Question:")
question_label.pack(anchor="w", padx=10, pady=5)

question_entry = ttk.Entry(root, width=50)
question_entry.pack(padx=10, pady=5)

# Submit Button
submit_button = ttk.Button(root, text="Get Answer", command=get_answer)
submit_button.pack(pady=10)

# Answer Label
answer_label = ttk.Label(root, text="Answer:", wraplength=550, justify="left", font=("Arial", 12, "italic"))
answer_label.pack(anchor="w", padx=10, pady=20)

# Run the main loop
root.mainloop()
