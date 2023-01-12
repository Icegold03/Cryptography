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
        return True
    else:
        return False


def make_server():
    socket.bind((pc_ip, portNumber))
    socket.listen()
    print('server made')

    while True:
        clientSocket, clientAddress = socket.accept()

        print ("Connection established with: ", clientAddress[0] + ":" + str(clientAddress[1]))

        thread = th.Thread(target=s.clientThread, args=(clientSocket, clientAddress, ))
        thread.start()


def send_public_agriments(g,p):
    pass

def resive_public_argriments():
    pass

def send_mix(T):
    pass

def recive_mix():
    pass