import socket as s
import socket_help_fucs as shf

class Client():
    def __init__(self, client_socket):
        self.client_socket = client_socket



    def recv_pup(self):
        g=int(shf.recv(self.client_socket))
        p=int(shf.recv(self.client_socket))
        return g, p

    def close(self):
        self.client_socket.shutdown(s.SHUT_RDWR)
        self.client_socket.close()
        print('connection closed')