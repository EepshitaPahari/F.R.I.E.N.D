import time
import max30100

# Initialize the MAX30100 sensor
mx30 = max30100.MAX30100()
mx30.enable_spo2()  # Enable SpO2 mode

def get_pulse():
    """
    Reads and returns the pulse rate from the MAX30100 sensor.
    """
    mx30.read_sensor()
    pulse = int(mx30.ir / 100)  # Calculate pulse rate from IR data
    return pulse

def get_SPO():
    """
    Reads and returns the SpO2 level from the MAX30100 sensor.
    """
    mx30.read_sensor()
    spo2 = int(mx30.red / 100)-15  # Calculate SpO2 from RED data
    
    if(spo2<0):
        return 0
    elif(spo2>100):
        return 100;
    else:
        return spo2# Ensure SpO2 is not negative

def get_temp():
    """
    Reads and returns the temperature from the MAX30100 sensor in °C.
    """
    temp = mx30.get_temperature()  # Retrieve temperature
    return temp
'''
if __name__ == "__main__":
    while True:
        pulse = get_pulse()
        spo2 = get_SPO()
        temperature = get_temp()

        print(f"Pulse: {pulse} BPM")
        print(f"SpO2: {spo2}%")
        print(f"Temperature: {temperature:.2f} °C")
        time.sleep(0.5)  # Delay between readings'''