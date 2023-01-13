
HEADERSIZE = 10

def add_header(msg):
    '''adds a header to af msg og lenght 10
    msg: string
    returns: string'''

    hmsg = f'{len(msg):<{HEADERSIZE}}'+msg
    print(hmsg)
    return hmsg


def send(socket, msg):
    '''send a msg to socket
    socket: objekt
    msg: string'''
    socket.send(bytes(msg,"utf-8"))
    

def recv(socket):
    '''recives a msg with header from socket 
    sokect: objekt
    returns: string, msg without header'''
    full_msg = ''
    new_msg = True
    while True:
        msg = socket.recv(16)
        if new_msg:
            #print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        #print(f"full message length: {msglen}")

        full_msg += msg.decode("utf-8")

        #print(len(full_msg))


        if len(full_msg)-HEADERSIZE == msglen:
            #print("full msg recvd")
            #print(full_msg[HEADERSIZE:])

            return full_msg[HEADERSIZE:]

