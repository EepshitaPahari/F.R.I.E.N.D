import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk

# Sample contacts dictionary to store contacts
contacts = {
    "Emergency Contact": "911",
    "Family Member 1": "123-456-7890",
    "Friend 1": "987-654-3210",
    "Neighbor": "555-555-5555"
}

# Function to show the contact list
def show_contact_list():
    def select_contact(event):
        selected_contact = listbox_contacts.get(tk.ACTIVE)
        if selected_contact:
            confirm_call = messagebox.askyesno("Make Call", f"Do you want to call {selected_contact}?")
            if confirm_call:
                make_call(selected_contact)

    # Create a new window for contact list display
    contact_list_window = tk.Toplevel()
    contact_list_window.title("Contact List")

    # Make the new window fullscreen
    contact_list_window.state('zoomed')

    # Create a listbox to display contacts with larger font
    listbox_contacts = tk.Listbox(contact_list_window, width=50, height=10, font=("Helvetica", 24))
    listbox_contacts.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    # Insert contacts into the listbox
    for contact in contacts:
        listbox_contacts.insert(tk.END, contact)

    # Bind double-click event to select contact
    listbox_contacts.bind("<Double-Button-1>", select_contact)

# Function to make a call
def make_call(contact_name):
    if contact_name in contacts:
        messagebox.showinfo("Calling", f"Calling {contact_name}: {contacts[contact_name]}", font=("Helvetica", 24))
    else:
        messagebox.showwarning("Not Found", "Contact not found.", font=("Helvetica", 24))

# Function for emergency call
def emergency_call():
    emergency_contact = "Emergency Contact"
    if emergency_contact in contacts:
        messagebox.showinfo("Emergency Call", f"Calling {emergency_contact}: {contacts[emergency_contact]}", font=("Helvetica", 24))
    else:
        messagebox.showwarning("Not Found", "Emergency contact not specified.", font=("Helvetica", 24))

# Create the main window
root = tk.Tk()
root.title("Elderly Contact Application")

# Full path to the background image
image_path = r"C:\Users\Eepshita\Desktop\FINAL YEAR PROJECT\F.R.I.E.N.D.png"

# Load and display background image
def resize_image(event):
    canvas.config(width=event.width, height=event.height)
    img = original_image.resize((event.width, event.height))
    bg_image = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
    canvas.image = bg_image  # Keep a reference to prevent garbage collection

try:
    original_image = Image.open(image_path)
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill="both", expand=True)
    root.bind("<Configure>", resize_image)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load image: {e}", font=("Helvetica", 24))

# Set a more aesthetic font
button_font = ("Helvetica", 24, "bold")

# Create a custom style for the buttons
style = ttk.Style()
style.configure('AccentButton.TButton', font=button_font, foreground="black", background="#FFD700", width=20)

# Create and place the buttons with custom style
button_show_list = ttk.Button(root, text="Show Contact List", command=show_contact_list, style='AccentButton.TButton')
button_show_list.place(relx=0.1, rely=0.5, anchor=tk.CENTER)

button_emergency_call = ttk.Button(root, text="Emergency Call", command=emergency_call, style='AccentButton.TButton')
button_emergency_call.place(relx=0.9, rely=0.5, anchor=tk.CENTER)

# Make the window fullscreen on startup
root.state('zoomed')

# Run the application
root.mainloop()
