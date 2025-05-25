from tkinter import *
import bcrypt

def validate(entered_password):
    hash = b'$2b$12$tPuCJnBTqcc97eF2WK42Keg9ZBL/vdnaPjJzYysKGhZZBO5DSPCmK'
    entered_password = bytes(entered_password, encoding='utf-8')
    if bcrypt.checkpw(entered_password, hash):
        status_label.config(text="Login Successful", fg="green")
    else:
        status_label.config(text="Login Failed", fg="red")

root = Tk()
root.geometry("250x200")
root.configure(bg="black")

# Password Entry
password_entry = Entry(root, show='*')
password_entry.pack(pady=10)

# Validate Button with beige foreground and black background
button = Button(root, text="Validate", bg="beige", fg="black", command=lambda: validate(password_entry.get()))
button.pack(pady=5)

# Label to display login result
bold_font = ('Arial', 10, 'bold')
status_label = Label(root, text="", bg="black", fg="white",font=bold_font)
status_label.pack(pady=10)

root.mainloop()
