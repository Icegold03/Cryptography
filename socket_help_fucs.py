
HEADERSIZE = 10


def add_header(msg: str) -> str:
    '''adds a header to af msg of lenght 10.
    The header tell how long the messge is.
    '''

    hmsg = f'{len(msg):<{HEADERSIZE}}'+msg
    # print(hmsg)
    return hmsg


def send(socket: object, msg: str) -> None:
    '''send a msg to socket with header'''
    socket.send(bytes(add_header(msg), "utf-8"))


def number_of_clients(socket: object) -> int:
    '''gets the number of clients conneted to the server'''

    # sends a requst to server
    # it send 'cl' without header
    socket.send(bytes('cl', "utf-8"))

    # recives af returns the number of clients on server
    return int(recv(socket))


def recv(socket: object) -> str:
    '''recives a msg with header from socket 
    sokect: objekt
    returns: string, msg without header'''

    full_msg = ''

    # Variable to check if a new message has arrived
    new_msg = True

    while True:
        msg = socket.recv(16) # Receive a message of up to 16 bytes

        # Extract the length of the message from the header
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        # Add the received message to full_msg
        full_msg += msg.decode("utf-8")

        # Check if the entire message has been received
        if len(full_msg)-HEADERSIZE == msglen:

            # if yes, return the message without the header
            return full_msg[HEADERSIZE:]
