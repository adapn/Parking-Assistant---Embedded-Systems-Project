import serial

try:
    while True: 
        ser = serial.Serial('COM3', 115200, timeout=1)  # Adjust COM port and baud rate
        print(ser.name)         # check which port was really used

        line = ser.readline().decode("utf-8")

        print(f"{line}")


        ser.close()      
except KeyboardInterrupt:
    print("Exiting...")

finally:
    ser.close