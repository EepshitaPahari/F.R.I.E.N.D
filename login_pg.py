import tkinter as tk
import os
from tkinter import ttk
from tkinter import Button, Tk, Toplevel, Label, Entry

def open_sign_in():
  sign_in_window = Toplevel()
  sign_in_window.title("Sign In")
  sign_in_window.geometry('500x300')
  sign_in_window.config(bg='black')

  username_label = Label(sign_in_window, text="Username:",fg="white",bg="black")
  username_label.grid(row=0,column=1,padx=10,pady=1)
  username_entry = Entry(sign_in_window)
  username_entry.grid(row=0,column=2,padx=1,pady=1)

  e_mail_label = Label(sign_in_window, text="E-mail:",fg="white",bg="black")
  e_mail_label.grid(row=1,column=1,padx=10,pady=1)
  e_mail_entry = Entry(sign_in_window) 
  e_mail_entry.grid(row=1,column=2,padx=1,pady=1)

  password_label = Label(sign_in_window, text="Password:",fg="white",bg="black")
  password_label.grid(row=2,column=1,padx=10,pady=1)
  password_entry = Entry(sign_in_window, show="*")  
  password_entry.grid(row=2,column=2,padx=1,pady=1)

  sign_in_button = Button(sign_in_window, text="Sign In",font='Calibri 8 italic', bg="blue", fg="white", command=lambda: handle_sign_in(username_entry.get(), e_mail_entry.get(), password_entry.get()))
  sign_in_button.grid(row=3,column=2,padx=100,pady=1)


# def handle_sign_in(username, e_mail,password):
#   print(f"Username: {username}, E_mail: {e_mail}, Password: {password}") 
def handle_sign_in(username, e_mail, password):
    
    if not username or not e_mail or not password:
        print("Error: All fields (username, e_mail, and password) are required.")
        return

    print(f"Username: {username}, E_mail: {e_mail}, Password: {password}")

    file_path = "credentials.txt"

    with open(file_path, "a") as file:
        file.write(f"Username: {username}, E_mail: {e_mail}, Password: {password}\n")

    print("Credentials have been saved to", file_path)

handle_sign_in("user123", "user123@example.com", "securepassword")


root = Tk()
root.geometry('500x300')
title_label=tk.Label(master=root,text='Create a new account',font='Calibri 24 italic',fg="white",bg="black")
title_label.place(anchor="center")
title_label.grid(row=3,column=3,padx=100,pady=50)
button = Button(master=root,text="sign in",font='Calibri 8 italic', bg="blue", fg="white",width=30, command=open_sign_in)
button.place(anchor='center')
button.grid(row=4,column=3,padx=10,pady=1)
root.configure(bg="black")

root.mainloop()
