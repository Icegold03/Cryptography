import socket as s
import threading as th

clients = set()

def clientThread(clientSocket, clientAddress):
    while True:
        message = clientSocket.recv(1024).decode("utf-8")
        print(clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+ message)
        for client in clients:
            if client is not clientSocket:
                client.send((clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+ message).encode("utf-8"))

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


while True:
    clientSocket, clientAddress = hostSocket.accept()
    clients.add(clientSocket)
    print ("Connection established with: ", clientAddress[0] + ":" + str(clientAddress[1]))
    print(clients)
    thread = th.Thread(target=clientThread, args=(clientSocket, clientAddress, ))
    thread.start()