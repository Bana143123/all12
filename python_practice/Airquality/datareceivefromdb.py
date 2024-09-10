import socket
import sqlite3
import time
import pandas as pd
import matplotlib.pyplot as plt

UDP_IP = "0.0.0.0"  # Listen on all available network interfaces
UDP_PORT = 5005

# Connect to SQLite database (or create it)
conn = sqlite3.connect('air_quality_data.db')
c = conn.cursor()

# Create table for storing data
c.execute('''CREATE TABLE IF NOT EXISTS air_quality
             (timestamp TEXT, temperature REAL, humidity REAL)''')

# Set up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on {UDP_IP}:{UDP_PORT}")

# Function to store data in the database
def store_data(temperature, humidity):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with conn:
        c.execute("INSERT INTO air_quality (timestamp, temperature, humidity) VALUES (?, ?, ?)",
                  (timestamp, temperature, humidity))

# Main loop to receive data and store it
while True:
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    data = data.decode()
    temperature, humidity = map(float, data.split(','))
    print(f"Received data: {temperature} C, {humidity} %")
    store_data(temperature, humidity)

    # Load data from the database
    df = pd.read_sql_query("SELECT * FROM air_quality", conn)

    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Plot data
    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['temperature'], label='Temperature (C)')
    plt.plot(df['timestamp'], df['humidity'], label='Humidity (%)')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Air Quality Monitoring')
    plt.legend()
    plt.show()
