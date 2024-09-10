import network
import socket
import time
from machine import Pin
from dht import DHT22

# Replace with your network credentials and the IP address of your computer
SSID = 'your_SSID'
PASSWORD = 'your_PASSWORD'
UDP_IP = "your_computer_ip"
UDP_PORT = 5005

# Initialize DHT22 sensor
dht_pin = Pin(4, Pin.IN)
dht_sensor = DHT22(dht_pin)

# Connect to WiFi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
    print('Connected to WiFi:', wlan.ifconfig())

connect_wifi(SSID, PASSWORD)

# Set up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Main loop to read sensor data and send it to the computer
while True:
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        
        data = f"{temperature},{humidity}"
        
        sock.sendto(data.encode(), (UDP_IP, UDP_PORT))
        print(f"Sent data: {data}")
        
    except Exception as e:
        print('Failed to read sensor or send data:', e)
    
    time.sleep(60)  # Wait for 1 minute before the next reading
