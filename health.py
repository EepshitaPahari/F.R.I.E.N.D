import tkinter as tk
import random
from testMAX30100 import get_pulse, get_SPO, get_temp


def run_patient_monitor():
    class PatientMonitor:
        def __init__(self, root):
            # Set the window size and remove the title bar
            root.geometry("480x320")  # Set window size to 480x320
            root.overrideredirect(1)  # Remove the title bar

            self.root = root
            self.root.configure(bg='black')  # Set background color to black

            # Define colors for each vital sign box
            self.colors = {
                'heart_rate': '#00FF00',  # Green
                'blood_pressure': '#00FFFF',  # Cyan
                'temperature': '#FFFF00',  # Yellow
                'respiration_rate': '#FF00FF',  # Magenta
                'oxygen_saturation': '#FF0000',  # Red
            }

            # Create vital sign frames
            self.heart_rate_frame = self.create_vital_frame("Heart Rate: -- bpm", self.colors['heart_rate'], row=0)
            self.blood_pressure_frame = self.create_vital_frame("Blood Pressure: --/-- mmHg", self.colors['blood_pressure'], row=1)
            self.temperature_frame = self.create_vital_frame("Temperature: -- °C", self.colors['temperature'], row=2)
            self.respiration_rate_frame = self.create_vital_frame("Respiration Rate: -- breaths/min", self.colors['respiration_rate'], row=3)
            self.oxygen_saturation_frame = self.create_vital_frame("Oxygen Saturation: -- %", self.colors['oxygen_saturation'], row=4)

            # Start updating the vital signs
            self.update_vitals()

        def create_vital_frame(self, initial_text, color, row):
            frame = tk.Frame(self.root, bg=color, padx=10, pady=5)
            frame.grid(row=row, column=0, padx=20, pady=10, sticky='ew')
            label = tk.Label(frame, text=initial_text, font=("Arial", 16), bg=color, fg='black')
            label.pack()
            return frame

        def update_vitals(self):
            # Simulate reading from sensors
            heart_rate = get_pulse()
            systolic_bp = random.randint(110, 130)
            diastolic_bp = random.randint(70, 90)
            temperature = get_temp()
            respiration_rate = random.randint(12, 20)
            oxygen_saturation = get_SPO()

            # Update labels with new values
            self.update_label(self.heart_rate_frame, f"Heart Rate: {heart_rate} bpm")
            self.update_label(self.blood_pressure_frame, f"Blood Pressure: {systolic_bp}/{diastolic_bp} mmHg")
            self.update_label(self.temperature_frame, f"Temperature: {temperature:.1f} °C")
            self.update_label(self.respiration_rate_frame, f"Respiration Rate: {respiration_rate} breaths/min")
            self.update_label(self.oxygen_saturation_frame, f"Oxygen Saturation: {oxygen_saturation} %")

            # Schedule the update_vitals function to run again after 1000ms (1 second)
            self.root.after(500, self.update_vitals)

        def update_label(self, frame, new_text):
            # Get the label from the frame and update its text
            label = frame.winfo_children()[0]
            label.config(text=new_text)

    root = tk.Tk()
    app = PatientMonitor(root)
    close_button = tk.Button(root, text='X', command=root.destroy, bg='red', fg='white')
    close_button.grid(row=0,column=3,pady=5, padx=5)
    root.mainloop()




