import tkinter as tk
from tkinter import messagebox

def show_name_fields():
    try:
        count = int(entry_people.get())
        if count < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of people.")
        return

    for widget in name_frame.winfo_children():
        widget.destroy()

    name_entries.clear()

    for i in range(count):
        tk.Label(name_frame, text=f"Name of person #{i+1}:", bg="#fef9ef").grid(row=i, column=0, pady=2, sticky="w")
        entry = tk.Entry(name_frame, font=("Arial", 11), width=25)
        entry.grid(row=i, column=1, padx=5, pady=2)
        name_entries.append(entry)

def calculate_split():
    try:
        total = float(entry_bill.get())
        if total <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid bill amount.")
        return

    names = [entry.get().strip() for entry in name_entries]
    if not all(names):
        messagebox.showwarning("Missing Info", "Please enter all names.")
        return

    num_people = len(names)
    share = round(total / num_people, 2)

    result_text = f"💰 Total Bill: ₹{total}\nEach Person Owes: ₹{share}\n\n"
    for name in names:
        result_text += f"{name} owes ₹{share}\n"

    result_label.config(text=result_text)

# GUI Setup
root = tk.Tk()
root.title("🍽️ Bill Splitter App")
root.geometry("450x550")
root.config(bg="#fef9ef")
root.resizable(False, False)

tk.Label(root, text="Split Your Bill Fairly!", font=("Helvetica", 16, "bold"), fg="#e11d48", bg="#fef9ef").pack(pady=15)

# Number of people
tk.Label(root, text="👥 Number of People:", font=("Arial", 12), bg="#fef9ef").pack()
entry_people = tk.Entry(root, font=("Arial", 12), justify="center")
entry_people.pack(pady=5)

tk.Button(root, text="➕ Add Name Fields", command=show_name_fields,
          font=("Arial", 11), bg="#4ade80", fg="white").pack(pady=10)

# Frame for dynamic name entries
name_frame = tk.Frame(root, bg="#fef9ef")
name_frame.pack(pady=5)
name_entries = []

# Bill amount
tk.Label(root, text="💵 Enter Bill Amount (₹):", font=("Arial", 12), bg="#fef9ef").pack(pady=10)
entry_bill = tk.Entry(root, font=("Arial", 12), justify="center")
entry_bill.pack(pady=5)

# Calculate Button
tk.Button(root, text="✅ Calculate Split", command=calculate_split,
          font=("Arial", 12), bg="#6366f1", fg="white").pack(pady=15)

# Results
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#fef9ef", justify="left", anchor="w")
result_label.pack(pady=10, padx=20, fill="both")

root.mainloop()
