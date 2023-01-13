import socket as s
import threading as th
import socket_help_fucs as shf
from generate_parameters import parameters

clients = set()

def clientThread(clientSocket, clientAddress):
    while True:
        message = clientSocket.recv(16).decode("utf-8")
        print(message)
        if message == 'cl':
            print('in if statment for respont on clients')
            shf.send(clientSocket, str(len(clients)))
            print('respont on clients send')
        else:
            for client in clients:
                if client is not clientSocket:
                    client.send( message.encode("utf-8") )

        if not message:
            clients.remove(clientSocket)
            print(clientAddress[0] + ":" + str(clientAddress[1]) +" disconnected")
            break

    clientSocket.close()

hostSocket = s.socket(s.AF_INET, s.SOCK_STREAM)
hostSocket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR,1)

hostIp=str(s.gethostbyname(s.gethostname() )) 
print(hostIp)

portNumber = 7500
hostSocket.bind((hostIp, portNumber))
hostSocket.listen()
print ("Waiting for connection...")

g, p = parameters()

while True:
    clientSocket, clientAddress = hostSocket.accept()
    clients.add(clientSocket)
    print ("Connection established with: ", clientAddress[0] + ":" + str(clientAddress[1]))
    print(str(len(clients)))
    shf.send(clientSocket, str(g))
    shf.send(clientSocket, str(p))
    thread = th.Thread(target=clientThread, args=(clientSocket, clientAddress, ))
    thread.start()