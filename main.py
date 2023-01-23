from random import randint
import tkinter as tk
import com


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root settings
        self.title('Diffie-Hellman key exchange')
        self.geometry('300x250')

        # header
        header = tk.Label(
            self, text='Diffie-Hellman key exchange', font=('Arial', 15))
        header.pack()

        # status text
        self.status_text_var = tk.StringVar()
        self.status_text_var.set('you are not connected')
        self.status = tk.Label(self, textvariable=self.status_text_var,
                               font=('Times New Roman', 15))
        self.status.pack()

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

        print("---- Diffie Hellman key excange started ----")

        # trys to connect to the a server with the ip addres from er entry
        print("Trying to connect to server")
        ip_addres = str(self.ip_entry.get())
        self.socket = com.try_server(ip_addres)

        # if no server was found, it returns
        if self.socket == None:
            self.status_text_var.set('no server found')
            print(f"No server found at IP: {ip_addres}")
            return
        print('server was found \n', )

        # when closing the tkinter window, call on_closing to close the sever connection
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # recive DH parameters from server
        print("Reciving parameters:")
        g, p = self.socket.recv_param()
        print(print_format("g", g))
        print(print_format("p", p))

        # generate random private number
        print("calculating:")
        s = randint(1, p-1)
        print(print_format("s", s))

        # take g to the power of s mod p
        A = pow(g, s, p)
        print(print_format("A", A))

        # Swap A with the other persen to get B
        print("trying to swap")
        B = self.socket.send_mix(A)
        print('swapt')
        print(print_format("B", B))

        # generate shared secret key
        # take B to the power of s mod p
        print("Shared key:")
        S = pow(B, s, p)
        print(print_format("S", S))

        print('---- Key exchange successful ----')
        self.status_text_var.set('Key exchange successful')

        self.kye_lable = tk.Label(
            self, text=f"Your shared key is: \n{S}", wraplength=180, justify="left")
        self.kye_lable.pack()

    def on_closing(self):
        self.socket.close()
        self.destroy()


def print_format(name: str, number: int) -> str:
    n = str(number)
    return f'-{name} (l: {len(n)}): {n[:5]}...'


if __name__ == "__main__":
    app = App()
    app.mainloop()
