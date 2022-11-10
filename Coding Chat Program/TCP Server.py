import socket
from datetime import datetime

HOST = '192.168.56.1'
PORT = 6789
MAX_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

print('Starting the server at: ', datetime.now())
print('Waiting for connection.....')

server.listen(5)
client, address = server.accept()

while True:
    data = client.recv(MAX_SIZE)
    if data.decode('utf-8') == "Quit":
        break
    print("At ", datetime.now(), address, "said ", data.decode('utf-8'))
    message_to_client = input('Enter Message to Client: ')
    message_to_client_encoded = message_to_client.encode('utf-8')
    client.send(message_to_client_encoded)
    if message_to_client == "Quit":
        break

client.close()
server.close()

