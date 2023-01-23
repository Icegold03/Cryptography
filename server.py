import socket as s
import threading as th
import socket_help_fucs as shf
from generate_parameters import parameters

# set of client_sockets
clients = set()

# make server socket
hostSocket = s.socket(s.AF_INET, s.SOCK_STREAM)
hostSocket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

# get ip addres for server
hostIp = str(s.gethostbyname(s.gethostname()))
print(hostIp)

# create server
portNumber = 7500
hostSocket.bind((hostIp, portNumber))
hostSocket.listen()
print("Waiting for connection...")

# get parameters
# thise are randomly generatet for each new server
g, p = parameters()


def run_server():
    """
    This function creates a server that listens for incoming connections on a specified IP address and port.
    When a client connects, it creates a thread for the client using the clientThread function and sends the client 
    the parameters g and p.
    """
    while True:
        # connect
        clientSocket, clientAddress = hostSocket.accept()
        clients.add(clientSocket)

        # print connection
        print("Connection established with: ",
              clientAddress[0] + ":" + str(clientAddress[1]))
        print('number of clients:', str(len(clients)))

        # send parmeters
        shf.send(clientSocket, str(g))
        shf.send(clientSocket, str(p))

        # make thread for client
        thread = th.Thread(target=clientThread, args=(
            clientSocket, clientAddress, ))
        thread.start()


def clientThread(clientSocket: s.socket, clientAddress: tuple):
    """
    This function creates a thread for each client that connects to the server. It receives messages from the client
    and broadcast it to all connected clients, except the sender. It also handles removing disconnected clients 
    from the clients set and closing the client socket.

    """
    while True:
        message = clientSocket.recv(16).decode("utf-8")
        print(message)
        if message == 'cl':
            shf.send(clientSocket, str(len(clients)))
            print('respont on clients send')
        else:
            for client in clients:
                if client is not clientSocket:
                    client.send(message.encode("utf-8"))

        if not message:
            clients.remove(clientSocket)
            print(clientAddress[0] + ":" +
                  str(clientAddress[1]) + " disconnected")
            break

    clientSocket.close()


if __name__ == "__main__":
    run_server()
