import tkinter as tk
from tkinter import messagebox
import random

# Global variables
score = 0
total = 0
num1 = num2 = correct_answer = 0

# Function to generate a new question
def generate_question():
    global num1, num2, operator, correct_answer
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)

    if operator == '+':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = num1 + num2
    elif operator == '-':
        num1 = random.randint(50, 100)
        num2 = random.randint(1, 49)
        correct_answer = num1 - num2
    elif operator == '*':
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        correct_answer = num1 * num2
    else:
        num1 = random.randint(10, 100)
        num2 = random.randint(1, 9)
        correct_answer = round(num1 / num2, 2)

    question_label.config(text=f"What is {num1} {operator} {num2}?")
    answer_entry.delete(0, tk.END)
    result_label.config(text="")

# Function to check the user's answer
def check_answer():
    global score, total
    try:
        user_answer = float(answer_entry.get())
        total += 1

        if round(user_answer, 2) == round(correct_answer, 2):
            score += 1
            result_label.config(text="✅ Correct!", fg="green")
        else:
            result_label.config(text=f"❌ Wrong! Answer: {correct_answer}", fg="red")

        score_label.config(text=f"Score: {score}/{total}")
        root.after(1500, generate_question)

    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number!")

# Function to restart the quiz
def restart_quiz():
    global score, total
    score = 0
    total = 0
    score_label.config(text="Score: 0/0")
    result_label.config(text="")
    generate_question()

# Main window setup
root = tk.Tk()
root.title("🧮 Math Quiz")
root.geometry("400x350")
root.config(bg="#dcf0f5")  

# Frame for central layout
frame = tk.Frame(root, bg="#f5f5dc", padx=20, pady=20)
frame.pack(expand=True)

# Title label
title = tk.Label(frame, text="Math Quiz", font=("Verdana", 22, "bold"), bg="#f5f5dc", fg="#333")
title.pack(pady=10)

# Question label
question_label = tk.Label(frame, text="", font=("Arial", 16), bg="#f5f5dc")
question_label.pack(pady=10)

# Entry for answer
answer_entry = tk.Entry(frame, font=("Arial", 14), justify="center", width=10, bd=2, relief="groove")
answer_entry.pack(pady=5)

# Submit button
check_button = tk.Button(frame, text="Submit Answer", font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white", padx=10, pady=5, command=check_answer)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(frame, text="", font=("Arial", 14), bg="#f5f5dc")
result_label.pack()

# Score label
score_label = tk.Label(frame, text="Score: 0/0", font=("Arial", 12), bg="#f5f5dc")
score_label.pack(pady=5)

# Restart button
restart_btn = tk.Button(frame, text="🔁 Restart Quiz", font=("Arial", 11), bg="#2196F3",
                        fg="white", padx=8, pady=4, command=restart_quiz)
restart_btn.pack(pady=10)

# Initialize first question
generate_question()

# Start the GUI loop
root.mainloop()


