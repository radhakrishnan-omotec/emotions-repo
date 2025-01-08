import socket
import csv
from datetime import datetime

# ESP32 IP and port
ESP32_IP = "192.168.0.140"  # Replace with the ESP32's IP
ESP32_PORT = 80

# CSV file to save data
csv_filename = "gsr_data.csv"

# Create a CSV file and write the header
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "GSR Value"])

try:
    # Connect to ESP32
    print("Connecting to ESP32...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ESP32_IP, ESP32_PORT))
    print("Connected!")

    while True:
        # Receive data
        data = client.recv(1024).decode("utf-8").strip()
        if data:
            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Print the received data
            print(f"Received: {data}")

            # Append data to the CSV file
            with open(csv_filename, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, data])

except KeyboardInterrupt:
    print("\nDisconnected!")
    client.close()
except Exception as e:
    print(f"An error occurred: {e}")
