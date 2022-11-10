import socket
from datetime import datetime

HOST = '192.168.56.1'
PORT = 6789
MAX_SIZE = 1024

print('Starting the client at:', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

while True:
    message_to_server = input("Enter Message to Server: ")
    message_to_server_encoded = message_to_server.encode('utf-8')
    client.send(message_to_server_encoded)
    if message_to_server == "Quit":
        break
    data = client.recv(MAX_SIZE)
    if data.decode('utf-8') == "Quit":
        break
    print("At ", datetime.now(), "server replied with ", data.decode('utf-8'))

client.close()
