import tkinter as tk
from tkinter import Button, Toplevel, Label, Entry, messagebox
from PIL import Image, ImageTk
from health import run_patient_monitor
import time
import threading
from playsound import playsound
import os
from meeting_app_2 import video_call
medication_entries = []
time_entries = []
# File path for saving medication data
file_path = "medication_data.txt"
# Function to open the medication page
def open_medication_page(username):
    medication_window = Toplevel()
    medication_window.geometry('480x320')
    medication_window.title('Medication Alarm')
    medication_window.config(bg="black")

    def add_on():
        submit()
    # Check if there are existing entries before trying to access them
        if len(medication_entries) > 0 and len(time_entries) > 0:
            # Get the current input values
            current_medication = medication_entries[-1].get()  # Access the most recent entry
            current_time = time_entries[-1].get()  # Access the most recent entry

            # If the fields are not empty, store them
        if current_medication and current_time:
           print(f"Medication Name: {current_medication}, Time: {current_time}")
        
        # Clear the current input fields
        medication_entries[-1].delete(0, tk.END)  # Clear the current medication entry
        time_entries[-1].delete(0, tk.END)  # Clear the current time entry
        
    # Add new medication name and time entry fields
    row = len(medication_entries) + 1  # Position below the previous entries



    med_label = Label(medication_window, text='Medicine name', font='Calibri 8 italic', fg="white", bg="black")
    med_label.grid(row=row, column=0, padx=2, pady=2, ipadx=5, ipady=2)

    med_entry = Entry(medication_window, width=10)
    med_entry.grid(row=row, column=1, padx=2, pady=2, ipadx=5, ipady=2)
    med_entry.bind("<FocusIn>", lambda event: set_focused_entry(med_entry))

    time_label = Label(medication_window, text='Time', font='Calibri 8 italic', fg="white", bg="black")
    time_label.grid(row=row, column=2, padx=2, pady=2, ipadx=5, ipady=2)

    time_entry = Entry(medication_window, width=10)
    time_entry.grid(row=row, column=3, padx=2, pady=2, ipadx=5, ipady=2)
    time_entry.bind("<FocusIn>", lambda event: set_focused_entry(time_entry))


    # Append the new entries to the lists
    medication_entries.append(med_entry)
    time_entries.append(time_entry)
    def set_focused_entry(entry):
        global focused_entry
        focused_entry = entry

    def insert_text(text):
        if focused_entry:
            focused_entry.insert(tk.END, text)

    def delete_last_character():
        if focused_entry:
            current = focused_entry.get()
            focused_entry.delete(0, tk.END)
            focused_entry.insert(0, current[:-1])

    def create_keyboard():
        keys = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ':', 'Space', 'Delete'
        ]

        # Set up the frame for the virtual keyboard
        keyboard_frame = tk.Frame(medication_window, bg="gray")
        keyboard_frame.grid(row=50, column=0, columnspan=4, sticky="nsew", pady=5)

        # Set initial row and column values
        col_val = 0
        row_val = 0

        # Adjust button size and layout for smaller device
        button_width = 1
        button_height = 1
        button_font = ('Arial', 8)  # Smaller font size

        for key in keys:
            if col_val > 9:  # Adjust for 10 columns max
                col_val = 0
                row_val += 1

            if key == "Space":
                # "Space" button spans 3 columns and uses less height
                button = Button(keyboard_frame, text="Space", width=5, height=1, font=button_font, command=lambda: insert_text(" "))
                button.grid(row=row_val, column=col_val, columnspan=3, padx=1, pady=2, sticky="ew")
                col_val += 3
            elif key == "Delete":
                # "Delete" button spans 3 columns and uses less height
                button = Button(keyboard_frame, text="Delete", width=5, height=1, font=button_font, command=delete_last_character)
                button.grid(row=row_val, column=col_val, columnspan=3, padx=1, pady=2, sticky="ew")
                col_val += 3
            else:
                # Standard button
                button = Button(keyboard_frame, text=key, width=button_width, height=button_height, font=button_font, command=lambda k=key: insert_text(k))
                button.grid(row=row_val, column=col_val, padx=1, pady=2, sticky="ew")
                col_val += 1

    def validate_time_format(alarm_time):
        """Validate the alarm time format (HH:MM)."""
        try:
            time.strptime(alarm_time, "%H:%M")
            return True
        except ValueError:
            return False

    def check_alarms():
        current_time = time.strftime("%H:%M")
        for time_entry in time_entries:
            alarm_time = time_entry.get().strip()
            if alarm_time == current_time:
                threading.Thread(target=playsound, args=("Audio.mp3",), daemon=True).start()
        # Schedule the next check
        medication_window.after(1000, check_alarms)

    def set_alarm(alarm_time):
        # Schedule the alarm check
        medication_window.after(1000, lambda: check_alarm_once(alarm_time))

    def check_alarm_once(alarm_time):
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            playsound("Audio.mp3")
        # Schedule the next check if needed (e.g., for recurring alarms)

    def submit():
        for med_entry, time_entry in zip(medication_entries, time_entries):
         med = med_entry.get()
         alarm_time = time_entry.get()
         if med and alarm_time:
            print(f"Medication Name: {med}, Alarm Time: {alarm_time}")
            # Start a new thread for each alarm
            threading.Thread(target=set_alarm, args=(alarm_time,), daemon=True).start()
            # Write the medication and time to the file
            with open(file_path, "a") as file:
                file.write(f"{med},{alarm_time}\n")
               
       
    add_on()
    check_alarms()
    create_keyboard()

    # Add button to add more entries
    add_button = Button(medication_window, text="Add", font='Calibri 8 bold', bg="blue", fg="white", command=add_on )
    add_button.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

    # Done button to save entries
    done_button = Button(medication_window, text="Done", font='Calibri 8 bold', bg="blue", fg="white", command=lambda: main_interface(username) )
    done_button.grid(row=0, column=3, padx=10, pady=10)

# Function definitions for main interface

def show_medication_management():
    medication_window = tk.Toplevel(root)
    medication_window.title("Medication")
    medication_window.config(bg="black")
    medication_window.geometry("480x320")
    tk.Label(medication_window, text="Upcoming Medications", font=("Arial", 20),bg="black",fg="white").grid(row=0, column=2,padx=2,pady=2)
    def delete_medication(index):
        """Delete the medication entry from the file and UI"""
        # Read current medication data
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Remove the medication and its time based on the index
        del lines[index]

        # Write back the updated data to the file
        with open(file_path, "w") as file:
            file.writelines(lines)

        # Update the medication window to reflect changes
        medication_window.destroy()
        show_medication_management()

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:
                for i, line in enumerate(lines):
                    # Strip leading/trailing whitespace and check if the line contains both medication and time
                    line = line.strip()
                    if line:  # Skip empty lines
                        parts = line.split(',')
                        if len(parts) == 2:  # Ensure the line has exactly two values
                            med, time = parts
                            
                            # Create labels to display medication and time
                            med_label = tk.Label(medication_window, text=f"Medication {i+1}: {med}", font=("Arial", 12), bg="black", fg="white")
                            med_label.grid(row=i + 1, column=1, padx=5, pady=5, sticky="w")
                            
                            time_label = tk.Label(medication_window, text=f"Time: {time}", font=("Arial", 12), bg="black", fg="white")
                            time_label.grid(row=i + 1, column=2, padx=5, pady=5, sticky="w")

                            # Create delete button for each medication entry
                            delete_button = tk.Button(medication_window, text="Delete", font=("Arial", 8), bg="red", fg="white",
                                                      command=lambda i=i: delete_medication(i))  # Pass the index to delete function
                            delete_button.grid(row=i + 1, column=3, padx=5, pady=5)
                        else:
                            print(f"Skipping malformed line: {line}")  # Debugging line
            else:
                tk.Label(medication_window, text="No medication data available", font=("Arial", 12), bg="black", fg="white").grid(row=1, column=1, columnspan=2, padx=5, pady=5)
    except FileNotFoundError:
        print("No medication data found.")
        tk.Label(medication_window, text="No medication data available", font=("Arial", 12), bg="black", fg="white").grid(row=1, column=1, columnspan=2, padx=5, pady=5)
           
    set_button = Button(medication_window, text="Set", bg="blue", fg="white", command=lambda: open_medication_page(username=''))
    set_button.grid(row=0, column=1)
def show_emergency():
    emergency_window=Toplevel()
    emergency_window.geometry('480x320')
    emergency_window.title('Emergency')
    lab=Label(emergency_window,text="Calling...",font="Calibri 32 bold")
    lab.grid(row=3,column=3,padx=5,pady=5)
    close_button = Button(emergency_window, text="X", command=emergency_window.destroy, bg='red', fg='white')
    close_button.grid(row=0,column=5)

def show_health_monitoring():
    health_monitoring_window = tk.Toplevel(root)
    health_monitoring_window.title("Health Monitoring")
    health_monitoring_window.geometry("480x320")
   # app = PatientMonitor(health_monitoring_window)
    health_monitoring_window.attributes('-toolwindow', True)  # Allow maximizing
    health_monitoring_window.resizable(True, True) # Allow maximizing
    # Add a back button
    back_button = Button(health_monitoring_window, text="Back", command=health_monitoring_window.destroy)
    back_button.pack(pady=20)

def show_communication():
    communication_window = tk.Toplevel(root)
    communication_window.title("Communication")
    communication_window.geometry("480x320")
    tk.Label(communication_window, text="Contact List", font=("Arial", 20),bg="white",fg="black").grid(row=0, column=2,padx=2,pady=2)

# Function to load and resize images
def load_and_resize_image(file_path, width, height):
    try:
        image = Image.open(file_path)
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image {file_path}: {e}")
        return None

# Function to display the main interface after sign-in and medication setup
def main_interface(username):
    main_window = tk.Toplevel()
    main_window.title("Elderly Assistance Device")
    main_window.geometry("480x320") 
    main_window.config(bg="black")

    # Load and resize Images
    img_width, img_height =70, 70 # Adjust the size as needed
    emergency_img = load_and_resize_image("emergency.jpg", img_width, img_height)
    health_monitoring_img = load_and_resize_image("health.jpg", img_width, img_height)
    medication_management_img = load_and_resize_image("medicine.jpg", img_width, img_height)
    communication_img = load_and_resize_image("communication.jpg", img_width, img_height)

    # Main Frame
    main_frame = tk.Frame(main_window,bg="black")
    main_frame.pack(pady=20)

    # Profile Section
    profile_frame = tk.Frame(main_frame)
    profile_frame.pack(pady=10)
    #tk.Label(profile_frame, text=f"Welcome, {username}", font=("Arial", 15,"italic"),bg="black",fg="white").pack()

    # Button Frame
    button_frame = tk.Frame(main_frame,bg="black")
    button_frame.pack(pady=5)

    # Emergency Button
    tk.Button(button_frame, command=show_emergency, image=emergency_img,bg="black", compound="left",  width=70, height=70).grid(row=1,column=1, padx=10,pady=1)
    tk.Label(button_frame,text="emergency",font=("Arial", 8,"italic"), fg="white",bg="black").grid(row=2,column=1,padx=10,pady=1)
    
    # Health Monitoring Button
    tk.Button(button_frame, command=run_patient_monitor, image=health_monitoring_img,bg="black", compound="left", width=70, height=70).grid(row=1,column=2, padx=10,pady=1)
    tk.Label(button_frame,text="health",font=("Arial", 8,"italic"), fg="white",bg="black").grid(row=2,column=2,padx=10,pady=1)
  
    # Medication Management Button
    tk.Button(button_frame, command=show_medication_management, image=medication_management_img, bg="black",compound="left", width=70, height=70).grid(row=3,column=1, padx=10,pady=1)
    tk.Label(button_frame,text="medication",font=("Arial", 8,"italic"), fg="white",bg="black").grid(row=4,column=1,padx=10,pady=1)
  
    # Communication Button
    tk.Button(button_frame, command=video_call, image=communication_img, compound="left",bg="black",width=70, height=70).grid(row=3,column=2, padx=10,pady=1)
    tk.Label(button_frame,text="communication",font=("Arial", 8,"italic"), fg="white",bg="black").grid(row=4,column=2,padx=10,pady=1)
   
    # Keep a reference to the images to prevent them from being garbage collected
    main_window.emergency_img = emergency_img
    main_window.health_monitoring_img = health_monitoring_img
    main_window.medication_management_img = medication_management_img
    main_window.communication_img = communication_img

# Main Application
root = tk.Tk()
root.title("Elderly Assistance Device")
root.geometry("480x320")
root.config(bg="black")

welcome_label = tk.Label(root, text="F.R.I.E.N.D", font=("Arial", 14,"italic"), fg="white",bg="black")
welcome_label.pack(pady=20)

sign_in_button = tk.Button(root, text="Sign In", command=lambda:open_medication_page(username=''), font=("Arial", 12,"italic"), bg="blue", fg="white")
sign_in_button.pack(pady=10)

root.mainloop()
