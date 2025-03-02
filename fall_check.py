import smbus
import math
import threading
import time
from notification import fall_noti

# MPU6050 Registers
MPU6050_ADDR = 0x68  # I2C address of the MPU6050
ACCEL_XOUT_H = 0x3B
PWR_MGMT_1 = 0x6B

# Initialize I2C communication
bus = smbus.SMBus(1)  # For Raspberry Pi, use I2C bus 1
def initialize_mpu6050():
    """
    Initializes the MPU6050 sensor by waking it up.
    """
    bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)  # Wake up the MPU6050

def read_raw_data(register):
    """
    Reads raw 16-bit data from the specified register.
    """
    high = bus.read_byte_data(MPU6050_ADDR, register)
    low = bus.read_byte_data(MPU6050_ADDR, register + 1)
    value = (high << 8) | low  # Combine high and low bytes
    # Convert to signed value
    if value > 32768:
        value -= 65536
    return value

def get_acceleration_data():
    """
    Reads and returns acceleration data from the MPU6050 sensor.
    """
    accel_x = read_raw_data(ACCEL_XOUT_H)
    accel_y = read_raw_data(ACCEL_XOUT_H + 2)
    accel_z = read_raw_data(ACCEL_XOUT_H + 4)

    # Convert raw data to 'g' units (sensitivity scale factor is 16384 for ±2g range)
    accel_x_g = accel_x / 16384.0
    accel_y_g = accel_y / 16384.0
    accel_z_g = accel_z / 16384.0

    return accel_x_g, accel_y_g, accel_z_g

def falling_check(accel_x, accel_y, accel_z, low_threshold=0.5, high_threshold=2.5):
    """
    Checks if a fall has occurred based on acceleration data.

    Parameters:
        accel_x (float): Acceleration in the X-axis (g).
        accel_y (float): Acceleration in the Y-axis (g).
        accel_z (float): Acceleration in the Z-axis (g).
        low_threshold (float): Lower threshold for free fall detection.
        high_threshold (float): Upper threshold for heavy impact detection.

    Returns:
        bool: True if a fall is detected, False otherwise.
    """
    # Calculate the magnitude of the acceleration vector
    magnitude = math.sqrt(accel_x**2 + accel_y**2 + accel_z**2)

    # Check if the magnitude indicates a fall (free fall or impact)
    return magnitude < low_threshold or magnitude > high_threshold

def fall_alert():
    """
    Continuously checks for falls using live accelerometer data from MPU6050.
    """
    initialize_mpu6050()
    print("Starting fall detection...")

    while True:
        # Get live acceleration data
        accel_x, accel_y, accel_z = get_acceleration_data()

        # Check for fall
        if falling_check(accel_x, accel_y, accel_z):
            print(f"Fall detected! Data: ({accel_x:.2f}, {accel_y:.2f}, {accel_z:.2f})")
            alert_thread = threading.Thread(target=fall_noti)
            alert_thread.start()
            alert_thread.join() 
           # break# Perform additional actions (e.g., send alert, log data, etc.)
        else:
            print(f"No fall detected. Data: ({accel_x:.2f}, {accel_y:.2f}, {accel_z:.2f})")

        # Add a small delay for efficiency
        time.sleep(0.1)
