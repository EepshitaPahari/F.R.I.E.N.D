from tkinter import Button, Tk, Toplevel, Label, Entry
def next():
  window=Toplevel()
  window.geometry('500x300')
  label=Label(window,text='Welcome User',font='Calibri 24 italic')
  label.pack()
  

def next_pg():
    next_window = Toplevel()
    next_window.geometry('500x300')
    label = Label(next_window, text="You are all set in",font='Calibri 24 italic')
    label.pack(padx=100,pady=100)
    next_button = Button(next_window,text="->",font='Calibri 10 bold ', bg="blue", fg="white",width=5,command=lambda:next())
    next_button.pack(side="bottom")

def add_on():
    medication_label=Label(root,text='Name of medicine',font='Calibri 8 italic')
    medication_label.pack()
    medication_entry = Entry(root)
    medication_entry.pack()

    time_label=Label(root,text='Time of dosage',font='Calibri 8 italic')
    time_label.pack()
    time_entry = Entry(root, width=10)
    time_entry.pack()  
def submit(med,time):
  med=medication_entry.get()
  time = time_entry.get()
  print(f"medication name: {med}, time: {time}") 
  next_pg()


root = Tk()
root.geometry('500x300')
root.title('Medication alarm')
medication_label=Label(root,text='Name of medicine',font='Calibri 8 italic')
medication_label.pack()
medication_entry = Entry(root)
medication_entry.pack()

time_label=Label(root,text='Time of dosage',font='Calibri 8 italic')
time_label.pack()
time_entry = Entry(root, width=10)
time_entry.pack()

button = Button(root,text="+",font='Calibri 8 bold ', bg="blue", fg="white",command=lambda:add_on())
button.pack()
skip_button = Button(master=root,text="skip",font='Calibri 8 italic', bg="blue", fg="white",command=lambda: next_pg())
skip_button.pack(side='right')
done_button = Button(master=root,text="done",font='Calibri 8 italic', bg="blue", fg="white",command=lambda: submit(medication_entry.get(), time_entry.get()))
done_button.pack(side='right')
root.mainloop()