import socket as s
import threading as th


class Client():
    def __init__(self, client_socket):
        self.client_socket = client_socket

    def close(self):
        self.client_socket.shutdown(s.SHUT_RDWR)
        self.client_socket.close()
        print('connection closed')


class Server():
    def __init__(self, pc_ip, portNumber):
        self.host_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.host_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

        self.host_socket.bind((pc_ip, portNumber))
        self.host_socket.listen()
        clients = set()
        print('server made')

        while True:
            clientSocket, clientAddress = self.host_socket.accept()
            clients.add(clientSocket)
            print ("Connection established with: ", clientAddress[0] + ":" + str(clientAddress[1]))
            print(clients)
            thread = th.Thread(target=self.clientThread, args=(clientSocket, clientAddress))
            thread.start()

    def clientThread(clientSocket, clientAddress):
        while True:
            message = clientSocket.recv(1024).decode("utf-8")
            print(clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+ message)




    def close(self):
        try:
            self.host_socket.shutdown(s.SHUT_RDWR)
            self.host_socket.close()
            print('server closed')
        except:
            print('nothing to close')
