from socket import * #from socket import all
serverName = 'localhost' #127.0.0.01
serverPort = 12000 #0-65000
clientSocket = socket(AF_INET, SOCK_DGRAM) #select ipv4(afnet) and socket kind UDP(SOCK_DGRAM)
message = input("Please type in your sentence: ") #.input() user input
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #2048 buffer size
print(modifiedMessage.decode())
clientSocket.close() #Closing socket