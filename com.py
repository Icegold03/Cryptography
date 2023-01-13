import socket as s
import threading as th
import com_class


portNumber = 7500
hostname=s.gethostname()   
pc_ip=str(s.gethostbyname(hostname)) 
print(pc_ip)

def try_server(ip):
    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    client_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

    try:
        client_socket.connect((ip, portNumber))
    except:
        print('no server was found')
        return None
        
    else:
        print('server found')
        return com_class.Client(client_socket)        



def send_mix(AB):
    pass

def recive_mix():
    pass