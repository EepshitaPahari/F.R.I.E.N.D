import time
#from noti_med import reminder
from buzzer import sound
#from tkinter import messagebox
#from noti_med import reminder
# Open the file that contains medication data
with open("medication_data.txt", "r") as file:
    lines = file.readlines()

def set_alarm():
    # Parse the medication and time data into a list of tuples
    medication_data = []
    for line in lines:
        medication, alarm_time = line.strip().split(",")  # Split line into medication and time
        try:
            time.strptime(alarm_time, "%H:%M")  # Validate time format
            medication_data.append((medication, alarm_time))
        except ValueError:
            print(f"Invalid time format for {medication}. Please ensure time is in HH:MM format.")
            continue  # Skip if time format is invalid

    current_time_pre = time.strftime("%H:%M")  # Initialize previous time

    while True:
        current_time = time.strftime("%H:%M")  # Get the current time in HH:MM format
        #print("waiting for alarm")
        if current_time != current_time_pre:  # Run only when the time changes
            current_time_pre = current_time  # Update the previous time
            
            for medication, alarm_time in medication_data:
                if current_time == alarm_time:
                    print(f"Time to take your medication: {medication}")
                    sound(medication)
                    #reminder()
                    # playsound("alarm_sound.mp3")  # Uncomment if you want sound alerts

    time.sleep(10)  # Sleep briefly to prevent excessive CPU usage
'''def ask_alarm():
    response= messagebox.askquestion("Medication_Alarm", "medicaiton_name", parent=None)
    if response == "Stop":
        #stop_alarm called
        print("alarm stop")    
'''
