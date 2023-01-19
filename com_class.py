from time import sleep
import socket as s
import socket_help_fucs as shf


class Client():
    '''class to handle communitation between client and server'''
    def __init__(self, client_socket: object) -> None:
        self.client_socket = client_socket

    def recv_param(self)-> tuple[int, int]:
        """recives HD parameters from server. Should be called right after conntion to server is made"""
        g=int(shf.recv(self.client_socket))
        p=int(shf.recv(self.client_socket))
        return g, p

    def send_mix(self, A:int)-> int:
        """
        This function is used to send A to the other clients on the server, and recive B.
        It first checks the number of clients connected to the server. If the number of clients is less than 2, it waits for 5 seconds and checks again.
        Once the number of clients is more than 1, it sends A to the server and receives B.
        """
        number_of_clients = 1

        while number_of_clients <2:
            number_of_clients = shf.number_of_clients(self.client_socket)
            sleep(2)

        shf.send(self.client_socket, str(A))
        return int(shf.recv(self.client_socket))

    

    def close(self):
        """
        This function is used to close the connection between the client and server.
        """
        self.client_socket.shutdown(s.SHUT_RDWR)
        self.client_socket.close()
        print('connection closed')