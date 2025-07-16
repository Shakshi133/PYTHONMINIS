import tkinter as tk
from tkinter import messagebox
import time
import threading

# Function to run the countdown in a separate thread
def start_timer():
    try:
        seconds = int(entry.get())
        if seconds < 1:
            messagebox.showwarning("Invalid Input", "Please enter a number greater than 0.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a whole number.")
        return

    def countdown():
        start_button.config(state="disabled")
        for remaining in range(seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            time_format = f"{mins:02}:{secs:02}"
            time_label.config(text=f"🕰️ Time left: {time_format}")
            time.sleep(1)
        time_label.config(text="⏰ Time's up! Take a break or move on to next task.")
        start_button.config(state="normal")

    # Run countdown in a thread to keep UI responsive
    threading.Thread(target=countdown).start()

# Setting up the GUI
root = tk.Tk()
root.title("⏳ Countdown Timer")
root.geometry("350x200")
root.resizable(False, False)

tk.Label(root, text="Enter time in seconds:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

start_button = tk.Button(root, text="Start Timer", command=start_timer, font=("Arial", 12), bg="green", fg="white")
start_button.pack(pady=10)

time_label = tk.Label(root, text="", font=("Arial", 14))
time_label.pack(pady=10)

root.mainloop()
