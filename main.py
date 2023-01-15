from random import randint
import tkinter as tk
import com


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root settings
        self.title('Diffie-Hellman key exchange')
        self.geometry('300x150')

        # header
        header = tk.Label(
            self, text='Diffie-Hellman key exchange', font=('Arial', 15))
        header.pack()

        # status text
        self.status_text_var = tk.StringVar()
        self.status_text_var.set('you are not connected')
        status = tk.Label(self, textvariable=self.status_text_var,
                          font=('Times New Roman', 15))
        status.pack()

        # ip addres input
        ip_input_frame = tk.Frame(self)
        connect_to_lable = tk.Label(ip_input_frame, text='Connect to')
        self.ip_entry = tk.Entry(ip_input_frame)
        self.ip_entry.insert(0, '192.168.1.231')
        connect_to_lable.grid(row=0, column=0)
        self.ip_entry.grid(row=0, column=1)
        ip_input_frame.pack()

        # connect button
        connect_btn = tk.Button(self, text='Connect',
                                command=self.start_key_exchange)
        connect_btn.pack(side='bottom', pady=10)

    def start_key_exchange(self):
        '''is called when the connect button get pushed. This function is responseble for making the key exchange '''

        # trys to connect to the a server with the ip addres from er entry
        ip_addres = str(self.ip_entry.get())
        self.socket = com.try_server(ip_addres)

        # if no server was found, it returns
        if self.socket == None:
            self.status_text_var.set('no server found')
            return

        # when closing the tkinter window, call on_closing to close the serer connection
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # recive DH parameters from server
        g, p = self.socket.recv_param()
        print('-g:', g)
        print('-p:', p)

        # generate random private number
        s = randint(1, p-1)
        print('-s:', s)

        # take g to the power of s mod p
        A = pow(g, s, p)
        print('-A:', A)

        # Swap A with the other persen to get B
        self.status_text_var.set('wating for swap')
        B = self.socket.send_mix(A)
        print('swapt')
        print('-B:', B)

        # generate shared secret key
        # take B to the power of s mod p
        S = pow(B, s, p)
        print('-S:', S)
        print('YOU WIN')
        self.key_exchange_sucesfull()

    def key_exchange_sucesfull(self):
        self.status_text_var.set('you are now conneted')

    def on_closing(self):
        self.socket.close()
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
