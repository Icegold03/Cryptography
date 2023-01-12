from socket import *
from tkinter import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "10.194.65.87"
hostIp = "10.194.65.87"
portNumber = 7500

clientSocket.connect((hostIp, portNumber))



def sendMessage(clientMessage):
    clientSocket.send(clientMessage.encode("utf-8"))


def recvMessage(app):
    while True:
        serverMessage = clientSocket.recv(1024).decode("utf-8")
        if len(serverMessage) >0 :
            app.show_smg(serverMessage)



