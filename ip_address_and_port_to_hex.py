import socket

from struct import pack


ip_address = "192.168.45.196"
port = 4444

print("IP Address: " +
      hex(int.from_bytes(socket.inet_aton(ip_address), byteorder="little")))
print("Port: " +
      hex(int.from_bytes(pack("<H", port))))

