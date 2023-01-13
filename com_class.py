import socket as s
import threading as th


class Client():
    def __init__(self, client_socket):
        self.client_socket = client_socket

    def close(self):
        self.client_socket.shutdown(s.SHUT_RDWR)
        self.client_socket.close()
        print('connection closed')