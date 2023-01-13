import socket as s
import socket_help_fucs as shf

class Client():
    def __init__(self, client_socket):
        self.client_socket = client_socket



    def recv_pup(self):
        msg=shf.recv(self.client_socket)
        #print(msg)
        return msg

    def close(self):
        self.client_socket.shutdown(s.SHUT_RDWR)
        self.client_socket.close()
        print('connection closed')