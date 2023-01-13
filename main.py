import tkinter as tk
import com
from random import randint


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Diffie-Hellman key exchange')
        self.geometry('300x150')

        header = tk.Label(self, text='Diffie-Hellman key exchange', font=('Arial', 15) )
        header.pack()

        self.status_text_var = tk.StringVar()
        self.status_text_var.set('you are not connected')
        status = tk.Label(self, textvariable=self.status_text_var, font=('Times New Roman', 15))
        status.pack()


        ip_input_frame = tk.Frame(self)
        connect_to_lable = tk.Label(ip_input_frame, text='Connect to')
        self.connect_to_input = tk.Entry(ip_input_frame)
        self.connect_to_input.insert(0, '192.168.1.231')
        connect_to_lable.grid(row=0, column=0)
        self.connect_to_input.grid(row=0, column=1)
        ip_input_frame.pack()

        connect_btn = tk.Button(self, text='Connect', command=self.start_key_exchange)
        connect_btn.pack(side = 'bottom', pady=10) 


    def start_key_exchange(self):
        ip_addres = str(self.connect_to_input.get())
        self.socket = com.try_server(ip_addres)
        if self.socket == None:
            return    
        self.protocol("WM_DELETE_WINDOW", self.on_closing) 

        g, p = self.socket.recv_param()
        print('-g:',g)
        print('-p:',p)

        s = randint(1,p-1)
        print('-s:',s)

        A = pow(g, s, p)
        print('-A:',A)

        B = self.socket.send_mix(A)
        print('swapt')
        print('-B:',B)

    def key_exchange_sucesfull(self):
        self.status_text_var.set('you are now conneted')

    def on_closing(self):
        self.socket.close()
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
