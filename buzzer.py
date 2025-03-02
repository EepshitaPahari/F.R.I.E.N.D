import RPi.GPIO as GPIO
import time
import tkinter as tk

BUZZER_PIN = 16

def buzzer_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    global pwm
    pwm = GPIO.PWM(BUZZER_PIN, 10)  # 10 Hz frequency
    pwm.start(60)  # 60% duty cycle
    print("Buzzer ON...")

def buzzer_off():
    global pwm
    pwm.stop()
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    #GPIO.cleanup()
    print("Buzzer OFF.")

def show_notification(med):
    root = tk.Tk()
    root.title("Medicine Reminder")
    root.geometry("480x320")

    label = tk.Label(root, text=f"Time to take medicine :  {med}", font=("Arial", 12))
    label.pack(pady=20)

    stop_button = tk.Button(root, text="Stop", command=lambda: on_stop(root), font=("Arial", 14), bg="red", fg="white")
    stop_button.pack(pady=10)

    root.mainloop()

def on_stop(root):
    buzzer_off()
    root.destroy()

def sound(med=""):
    buzzer_on()
    show_notification(med)

#if __name__ == "__main__":
    # Call set_alarm directly in the main thread.
#sound()
