import serial
import csv
import time
import datetime

SERIAL_PORT = 'COM4'
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

currentDate = datetime.datetime.now()
currentTime = currentDate.strftime("%m-%d-%Y %I-%M%p")

with open(f"C:/Users/Admin/Desktop/2025 Laboratory/Pressure Sensor/Pressure Logger/Results/Pressure Data from {currentTime}.csv", mode='w', newline='') as file:
    print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud")
    
    writer = csv.writer(file)
    writer.writerow(["Pressure_PSI", "Pressure_BAR"])

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()

            if "Pressure_PSI:" in line and "Pressure_BAR:" in line:
                parts = line.split(',')
                pressure_psi = parts[0].split(':')[1].strip()
                pressure_bar = parts[1].split(':')[1].strip()

                writer.writerow([pressure_psi, pressure_bar])
                print(f"Pressure_PSI: {pressure_psi}, Pressure_BAR: {pressure_bar}")
                
                time.sleep(1)
