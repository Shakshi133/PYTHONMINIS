import tkinter as tk
from tkinter import messagebox


def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10

    return min(score, 100)


def calculate_score():
    name1 = entry1.get().strip()
    name2 = entry2.get().strip()

    if not name1 or not name2:
        messagebox.showwarning("Oops!", "Please enter both names 💌")
        return

    score = friendship_score(name1, name2)
    result_label.config(
        text=f"💞 Friendship Score: {score} / 100 💞",
        fg="white",
        bg="#d946ef"
    )


root = tk.Tk()
root.title("💖 Friendship Calculator 💖")
root.geometry("450x380")
root.config(bg="#fce7f3")
root.resizable(False, False)


tk.Label(root, text="💕 Friendship Compatibility Calculator 💕",
         font=("Comic Sans MS", 16, "bold"), bg="#fce7f3", fg="#9d174d").pack(pady=20)
tk.Label(root, text="👧 Enter First Name:", font=("Arial", 12, "bold"),
         bg="#fce7f3", fg="#7e22ce").pack()
entry1 = tk.Entry(root, font=("Arial", 13), justify="center", bd=2, relief="groove")
entry1.pack(pady=8)
tk.Label(root, text="👦 Enter Second Name:", font=("Arial", 12, "bold"),
         bg="#fce7f3", fg="#7e22ce").pack()
entry2 = tk.Entry(root, font=("Arial", 13), justify="center", bd=2, relief="groove")
entry2.pack(pady=8)
tk.Button(root, text="💘 Calculate Score 💘", command=calculate_score,
          font=("Arial", 12, "bold"), bg="#ec4899", fg="white", padx=10, pady=5,
          relief="raised", bd=3, activebackground="#f472b6").pack(pady=20)
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"),
                        bg="#fce7f3", fg="#22c55e")
result_label.pack(pady=10)
root.mainloop()
