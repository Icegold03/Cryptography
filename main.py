import tkinter as tk
import client
import threading as th


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("test")

        btn = tk.Button(self, text="send", command=self.send).pack()

        recvThread = th.Thread(target=client.recvMessage(self))
        recvThread.daemon = True
        recvThread.start()


    def send(self):
        client.sendMessage("test")

    def show_msg(self, msg):
        print(msg)


if __name__ == "__main__":
    app = App()
    app.mainloop()
