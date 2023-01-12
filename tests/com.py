import socket as s
import threading as th

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)


portNumber = 7500
hostname=s.gethostname()   
pc_ip=str(s.gethostbyname(hostname)) 
print(pc_ip)

def try_server(ip):
    try:
        socket.connect((ip, portNumber))
    except:
        print('no server was found')
        socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
        return False
    else:
        return True


def make_server():
    socket.bind((pc_ip, portNumber))
    socket.listen()
    clients = set()
    print('server made')

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


    while True:
        clientSocket, clientAddress = socket.accept()
        clients.add(clientSocket)
        print ("Connection established with: ", clientAddress[0] + ":" + str(clientAddress[1]))
        print(clients)
        thread = th.Thread(target=clientThread, args=(clientSocket, clientAddress, ))
        thread.start()






def send_public_agriments(g,p):
    pass

def resive_public_argriments():
    pass

def send_mix(T):
    pass

def recive_mix():
    pass