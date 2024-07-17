import tkinter as tk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PatientMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Monitor")
        self.root.configure(bg='black')  # Set background color to black

        # Define colors for each vital sign box
        self.colors = {
            'heart_rate': '#00FF00',  # Green
            'blood_pressure': '#00FFFF',  # Cyan
            'temperature': '#FFFF00',  # Yellow
            'respiration_rate': '#FF00FF',  # Magenta
            'oxygen_saturation': '#FF0000',  # Red
        }

        # Create graph frames and vital sign frames
        self.heart_rate_graph_frame = self.create_graph_frame(row=0)
        self.respiration_rate_graph_frame = self.create_graph_frame(row=1)
        self.blood_pressure_graph_frame = self.create_graph_frame(row=2)
        self.temperature_graph_frame = self.create_graph_frame(row=3)
        self.oxygen_saturation_graph_frame = self.create_graph_frame(row=4)

        self.heart_rate_frame = self.create_vital_frame("Heart Rate: -- bpm", self.colors['heart_rate'], row=0)
        self.blood_pressure_frame = self.create_vital_frame("Blood Pressure: --/-- mmHg", self.colors['blood_pressure'], row=1)
        self.temperature_frame = self.create_vital_frame("Temperature: -- °C", self.colors['temperature'], row=2)
        self.respiration_rate_frame = self.create_vital_frame("Respiration Rate: -- breaths/min", self.colors['respiration_rate'], row=3)
        self.oxygen_saturation_frame = self.create_vital_frame("Oxygen Saturation: -- %", self.colors['oxygen_saturation'], row=4)

        # Create matplotlib figures with customized size and background color
        fig_width = 10 # Adjusted width of the figure
        fig_height = 2  # Adjusted height of the figure
        self.heart_rate_fig, self.heart_rate_ax = plt.subplots(figsize=(fig_width, fig_height), facecolor='black')
        self.respiration_rate_fig, self.respiration_rate_ax = plt.subplots(figsize=(fig_width, fig_height), facecolor='black')
        self.blood_pressure_fig, self.blood_pressure_ax = plt.subplots(figsize=(fig_width, fig_height), facecolor='black')
        self.temperature_fig, self.temperature_ax = plt.subplots(figsize=(fig_width, fig_height), facecolor='black')
        self.oxygen_saturation_fig, self.oxygen_saturation_ax = plt.subplots(figsize=(fig_width, fig_height), facecolor='black')

        # Set the background color of the axes
        self.heart_rate_ax.set_facecolor('black')
        self.respiration_rate_ax.set_facecolor('black')
        self.blood_pressure_ax.set_facecolor('black')
        self.temperature_ax.set_facecolor('black')
        self.oxygen_saturation_ax.set_facecolor('black')

        # Embed the figures in Tkinter canvases
        self.heart_rate_canvas = FigureCanvasTkAgg(self.heart_rate_fig, master=self.heart_rate_graph_frame)
        self.respiration_rate_canvas = FigureCanvasTkAgg(self.respiration_rate_fig, master=self.respiration_rate_graph_frame)
        self.blood_pressure_canvas = FigureCanvasTkAgg(self.blood_pressure_fig, master=self.blood_pressure_graph_frame)
        self.temperature_canvas = FigureCanvasTkAgg(self.temperature_fig, master=self.temperature_graph_frame)
        self.oxygen_saturation_canvas = FigureCanvasTkAgg(self.oxygen_saturation_fig, master=self.oxygen_saturation_graph_frame)

        self.heart_rate_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.respiration_rate_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.blood_pressure_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.temperature_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.oxygen_saturation_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Initialize data lists
        self.heart_rate_data = [random.randint(60, 100) for _ in range(100)]
        self.respiration_rate_data = [random.randint(12, 20) for _ in range(100)]
        self.blood_pressure_data = [(random.randint(110, 130), random.randint(70, 90)) for _ in range(100)]
        self.temperature_data = [random.uniform(36.5, 37.5) for _ in range(100)]
        self.oxygen_saturation_data = [random.randint(95, 100) for _ in range(100)]

        # Start updating the vital signs and graphs
        self.update_vitals()
        self.update_graphs()

    def create_vital_frame(self, initial_text, color, row):
        frame = tk.Frame(self.root, bg=color, padx=10, pady=5)
        frame.grid(row=row, column=1, padx=20, pady=10, sticky='ew')
        label = tk.Label(frame, text=initial_text, font=("Arial", 16), bg=color, fg='black')
        label.pack()
        return frame

    def create_graph_frame(self, row):
        frame = tk.Frame(self.root, bg='black', padx=10, pady=5)
        frame.grid(row=row, column=0, padx=20, pady=10, sticky='nsew')
        return frame

    def update_vitals(self):
        # Simulate reading from sensors
        heart_rate = random.randint(60, 100)
        systolic_bp = random.randint(110, 130)
        diastolic_bp = random.randint(70, 90)
        temperature = random.uniform(36.5, 37.5)
        respiration_rate = random.randint(12, 20)
        oxygen_saturation = random.randint(95, 100)

        # Update labels with new values
        self.update_label(self.heart_rate_frame, f"Heart Rate: {heart_rate} bpm")
        self.update_label(self.blood_pressure_frame, f"Blood Pressure: {systolic_bp}/{diastolic_bp} mmHg")
        self.update_label(self.temperature_frame, f"Temperature: {temperature:.1f} °C")
        self.update_label(self.respiration_rate_frame, f"Respiration Rate: {respiration_rate} breaths/min")
        self.update_label(self.oxygen_saturation_frame, f"Oxygen Saturation: {oxygen_saturation} %")

        # Add new data points to the lists
        self.heart_rate_data.append(heart_rate)
        self.heart_rate_data.pop(0)
        self.respiration_rate_data.append(respiration_rate)
        self.respiration_rate_data.pop(0)
        self.blood_pressure_data.append((systolic_bp, diastolic_bp))
        self.blood_pressure_data.pop(0)
        self.temperature_data.append(temperature)
        self.temperature_data.pop(0)
        self.oxygen_saturation_data.append(oxygen_saturation)
        self.oxygen_saturation_data.pop(0)

        # Schedule the update_vitals function to run again after 1000ms (1 second)
        self.root.after(1000, self.update_vitals)

    def update_label(self, frame, new_text):
        # Get the label from the frame and update its text
        label = frame.winfo_children()[0]
        label.config(text=new_text)

    def update_graphs(self):
        # Clear previous plots
        self.heart_rate_ax.clear()
        self.respiration_rate_ax.clear()
        self.blood_pressure_ax.clear()
        self.temperature_ax.clear()
        self.oxygen_saturation_ax.clear()

        # Plot new data
        self.heart_rate_ax.plot(self.heart_rate_data, color='green')
        self.respiration_rate_ax.plot(self.respiration_rate_data, color='magenta')
        self.blood_pressure_ax.plot([bp[0] for bp in self.blood_pressure_data], color='cyan', label='Systolic')
        self.blood_pressure_ax.plot([bp[1] for bp in self.blood_pressure_data], color='blue', label='Diastolic')
        self.temperature_ax.plot(self.temperature_data, color='yellow')
        self.oxygen_saturation_ax.plot(self.oxygen_saturation_data, color='red')

        # Set graph titles and labels
        self.heart_rate_ax.set_title('Heart Rate Over Time', color='white')
        self.respiration_rate_ax.set_title('Respiration Rate Over Time', color='white')
        self.blood_pressure_ax.set_title('Blood Pressure Over Time', color='white')
        self.temperature_ax.set_title('Temperature Over Time', color='white')
        self.oxygen_saturation_ax.set_title('Oxygen Saturation Over Time', color='white')

        # Add legends to blood pressure graph
        self.blood_pressure_ax.legend(facecolor='black', framealpha=1, edgecolor='white', labelcolor='white')

        # Set the color of the ticks and labels
        for ax in [self.heart_rate_ax, self.respiration_rate_ax, self.blood_pressure_ax, self.temperature_ax, self.oxygen_saturation_ax]:
            ax.tick_params(colors='white')
            ax.xaxis.label.set_color('white')
            ax.yaxis.label.set_color('white')

        # Draw the updated plots
        self.heart_rate_canvas.draw()
        self.respiration_rate_canvas.draw()
        self.blood_pressure_canvas.draw()
        self.temperature_canvas.draw()
        self.oxygen_saturation_canvas.draw()

        # Schedule the update_graphs function to run again after 1000ms (1 second)
        self.root.after(1000, self.update_graphs)

if __name__ == "__main__":
    root = tk.Tk()
    app = PatientMonitor(root)
    root.mainloop()
