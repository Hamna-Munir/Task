import socket
import uuid

# IP Address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("IP Address:", ip_address)

# MAC Address
mac = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff)
                for i in range(0, 8*6, 8)][::-1])
print("MAC Address:", mac)
