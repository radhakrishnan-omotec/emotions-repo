import socket
import csv
from datetime import datetime

# Server Configuration
HOST = "192.168.0.105"  # Ensure this is the correct IP of your server machine (laptop)
PORT = 12345            # Same port as defined in ESP32 code

# CSV File Setup
csv_file = "gsr_data.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "GSR Value"])  # Add headers

# Start Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}...")

try:
    while True:
        # Wait for a client connection
        print("Waiting for a connection...")
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        try:
            # Receive the data from the ESP32
            data = client_socket.recv(1024).decode().strip()
            if data:
                print(f"Received GSR Value: {data}")
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # Save to CSV
                with open(csv_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([timestamp, data])
                
                print(f"Data saved to CSV: {timestamp} - {data}")
            else:
                print("No data received from the client.")
        
        except Exception as e:
            print(f"Error receiving data: {e}")
        
        finally:
            # Always close the client connection after each transaction
            client_socket.close()
            print("Client disconnected.")

except KeyboardInterrupt:
    print("\nServer stopped.")
    server_socket.close()
