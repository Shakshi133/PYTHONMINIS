from tkinter import *
import bcrypt

def validate():
    password=password_entry.get()
    password_b=bytes(password,encoding='utf-8')
    hash=b'$2b$12$gYiMa3srhEsN1qCIZEaC8uFnzoasciF5488vrGyZyA00F.F7FvOea'

    if bcrypt.checkpw(password_b,hash):
        print('Login Successfully')
    else:
        print("Incorrect password")



root=Tk()
root.geometry("300x300")
password_entry=Entry(root)
password_entry.pack()
root.title("Password validator")

button=Button(root, text="Validate",command=lambda: validate())
button.pack()
root.mainloop()