#UDPClient.py
import time
from socket import *
serverName = 'localhost' #127.0.0.01
serverPort = 12000 #Range: 0-65000
clientSocket = socket(AF_INET, SOCK_DGRAM) #select ipv4(afnet) and socket kind UDP(SOCK_DGRAM)
for sequence_number in range(1,11):
    # Record start time
    send_time = time.time()
    # Construct message
    message = f'Ping {sequence_number} {send_time}'
    try:
        # Sending message to server
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        # Waiting for response
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        # Decoding and printing message
        print(f'Server Response:\n {modifiedMessage.decode()}')
        # Calculating RTT
        rtt = time.time() - send_time
        print(f"RTT = {rtt}")
    except timeout:
        print('Request Timed Out')
# Closing socket
clientSocket.close() #Closing socket