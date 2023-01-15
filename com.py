import socket as s
import com_class

# the prot the connection will be running on 
portNumber = 7500

#hostname=s.gethostname()   
#pc_ip=str(s.gethostbyname(hostname)) 
#print(pc_ip)

def try_server(ip:str):
    '''trys to connetc to af server with the given ip
    ip: the ip of the server to connect to'''

    # create a socket object
    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    client_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

    try:
        # try to connect to the server using the IP 
        client_socket.connect((ip, portNumber))
    except:
        # if no server was found, return
        print('no server was found')
        return None
        
    else:
        # if server was found, return instenc of the client class
        print('server found')
        return com_class.Client(client_socket)        
