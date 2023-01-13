import socket as s
import socket_help_fucs as shf
from time import sleep

class Client():
    def __init__(self, client_socket):
        self.client_socket = client_socket



    def recv_param(self):
        g=int(shf.recv(self.client_socket))
        p=int(shf.recv(self.client_socket))
        return g, p

    def send_mix(self, A):
        number_of_clients = 1
        while number_of_clients <2:
            number_of_clients = shf.number_of_clients(self.client_socket)
            print('number_of_clients:', number_of_clients)
            sleep(5)

        shf.send(self.client_socket, str(A))
        return shf.recv(self.client_socket)

    

    def close(self):
        self.client_socket.shutdown(s.SHUT_RDWR)
        self.client_socket.close()
        print('connection closed')