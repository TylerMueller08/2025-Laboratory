import serial
import csv
import time
import datetime

SERIAL_PORT = 'COM5'
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

currentDate = datetime.datetime.now()
currentTime = currentDate.strftime("%m-%d-%Y %I-%M%p")

with open(f"C:/Users/Admin/Desktop/2025 Laboratory/Scale Logger/Results/Scale Data from {currentTime}.csv", mode='w', newline='') as file:
    print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud")
    
    writer = csv.writer(file)
    writer.writerow(["WEIGHT_GRAMS"])

    while True:
        if ser.in_waiting > 0:
            raw_line = ser.readline().decode('ascii', errors='ignore').strip()
            if raw_line:
                print(f"Raw: {raw_line}")
                writer.writerow([raw_line])
        time.sleep(1)
