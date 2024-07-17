import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from PIL import ImageDraw


# Function definitions
def show_emergency():
    messagebox.showinfo("Emergency", "Emergency services have been contacted.")

def show_health_monitoring():
    health_monitoring_window = tk.Toplevel(root)
    health_monitoring_window.title("Health Monitoring")
    health_monitoring_window.geometry("400x300")
    tk.Label(health_monitoring_window, text="Health Metrics", font=("Arial", 20)).pack(pady=10)
    tk.Label(health_monitoring_window, text="Heart Rate: 72 bpm").pack(pady=5)
    tk.Label(health_monitoring_window, text="Blood Pressure: 120/80 mmHg").pack(pady=5)

def show_medication_management():
    medication_window = tk.Toplevel(root)
    medication_window.title("Medication")
    medication_window.geometry("400x300")
    tk.Label(medication_window, text="Medications", font=("Arial", 20)).pack(pady=10)
    tk.Label(medication_window, text="8:00 AM - Aspirin").pack(pady=10)
    tk.Label(medication_window, text="2:00 PM - Metformin").pack(pady=5)

def show_communication():
    communication_window = tk.Toplevel(root)
    communication_window.title("Communication")
    communication_window.geometry("400x300")
    tk.Label(communication_window, text="Communication", font=("Arial", 20)).pack(pady=10)
    tk.Button(communication_window, text="Video Call", command=show_video_call).pack(pady=5)
    tk.Button(communication_window, text="Call a contact", command=show_call_contact).pack(pady=5)

def show_video_call():
    messagebox.showinfo("Video Call", "Starting video call...")

def show_call_contact():
    messagebox.showinfo("Call a contact", "Starting call...")


# Function to load and resize images
def load_and_resize_image(file_path, width, height):
    try:
        image = Image.open(file_path)
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image {file_path}: {e}")
        return None

# Main Application Window
root = tk.Tk()
root.title("Elderly Assistance Device")
root.geometry("800x200")  # Adjusted window size to accommodate horizontal layout

# Load and resize Images
img_width, img_height = 40, 40  # Adjust the size as needed
emergency_img = load_and_resize_image("python\emergency.jpg", img_width, img_height)
health_monitoring_img = load_and_resize_image("python\healthmonitor.png", img_width, img_height)
medication_management_img = load_and_resize_image("python\medicine.jpeg", img_width, img_height)
communication_img = load_and_resize_image("python\comm.png", img_width, img_height)


# Main Frame
main_frame = tk.Frame(root)
main_frame.pack(pady=20)

# Profile Section
profile_frame = tk.Frame(main_frame)
profile_frame.pack(pady=10)
tk.Label(profile_frame, text="Welcome, John Doe", font=("Arial", 20)).pack()

# Button Frame
button_frame = tk.Frame(main_frame)
button_frame.pack(pady=10)

# Emergency Button
tk.Button(button_frame, text="Emergency", command=show_emergency, image=emergency_img, compound="left", bg="red", fg="white", font=("Arial", 15), width=200, height=50).pack(side=tk.LEFT, padx=10)

# Health Monitoring Button
tk.Button(button_frame, text="Health Monitoring", command=show_health_monitoring, image=health_monitoring_img, compound="left", font=("Arial", 15), width=200, height=50).pack(side=tk.LEFT, padx=10)

# Medication Management Button
tk.Button(button_frame, text="Medication", command=show_medication_management, image=medication_management_img, compound="left", font=("Arial", 15), width=200, height=50).pack(side=tk.LEFT, padx=10)

# Communication Button
tk.Button(button_frame, text="Communication", command=show_communication, image=communication_img, compound="left", font=("Arial", 15), width=200, height=50).pack(side=tk.LEFT, padx=10)


# Profile Section
profile_frame = tk.Frame(main_frame)
profile_frame.pack(pady=10)
tk.Label(profile_frame, text="Have a good day", font=("Arial", 20)).pack()


# Run the application
root.mainloop()