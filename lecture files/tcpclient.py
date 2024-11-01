from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Please type a sentence: ")
clientSocket.send(sentence.encode()) #Sending to server
modifiedSentence = clientSocket.recv(1024)#listening for a return
print(modifiedSentence)
clientSocket.close() #closing out socket