from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM for TCP
serverSocket.bind(('',serverPort))
serverSocket.listen(1) #activly listen from the stream
print('The server is ready')
while True:
    connectionSocket, addr = serverSocket.accept() #Create and accept the connection from client
    message = connectionSocket.recv(1024).decode() #get data from buffer and decode
    modifiedMessage = message.upper() #changing to uppercase
    connectionSocket.send(modifiedMessage.encode()) #sending back encoded message
    connectionSocket.close() #close connection to client
#notice how b'' is added to the sentence