import tkinter as tk

# Functions to increase and decrease the counter
def increase():
    global count 
    count += 1
    label.config(text=str(count))

def decrease():
    global count 
    count -= 1
    label.config(text=str(count))

# Set up the main window
root = tk.Tk()
root.title("Counter")
root.geometry("400x300")
root.resizable(False,False)
root.configure(bg="#f0f8ff")  # light background color

count = 0

# Style for label
label = tk.Label(root, text=str(count), font=("Helvetica", 48, "bold"), fg="#050E49", bg="#f0f8ff")
label.pack(pady=30)

# Frame to hold buttons
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

#buttons for increasing and decreasing the counter
increase_btn = tk.Button(button_frame, text="➕ Increase", font=("Arial", 14, "bold"), bg="#4caf50", fg="white", padx=10, pady=5, command=increase)
increase_btn.grid(row=0, column=0, padx=10)

decrease_btn = tk.Button(button_frame, text="➖ Decrease", font=("Arial", 14, "bold"), bg="#f44336", fg="white", padx=10, pady=5, command=decrease)
decrease_btn.grid(row=0, column=1, padx=10)

# Run the app
root.mainloop()
