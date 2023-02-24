import socket
import threading
import tkinter as tk
from tkinter import font
from tkinter import ttk


class CLIENT:

    def __init__(self):
        self.PORT = 5050
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

        self.window = tk.Tk()
        self.window.withdraw()

        self.login = tk.Toplevel()

        self.login.title("Login")

        self.login.resizable(width=False,
                             height=False)
        self.login.configure(width=400,
                             height=300)

        self.info = tk.Label(master=self.login, text="Login in order to continue!", font=("Aerial", 26))
        self.info.place(relheight=0.15,
                        relx=0,
                        rely=0.07)

        self.text_entry = tk.Entry(master=self.login, font=("Aerial", 26))
        self.text_entry.pack()
        self.text_entry.place(relwidth=0.4,
                              relheight=0.2,
                              relx=0.3,
                              rely=0.4,
                              )
        self.button = tk.Button(master=self.login, text="Submit", bg="black", fg="white",font=("Aerial",20),
                                command=lambda: self.next_scene(self.text_entry.get()))
        self.button.place(relwidth=0.4,
                          relheight=0.25,
                          relx=0.3,
                          rely=0.6)
        self.window.mainloop()

    def next_scene(self, name):
        self.client.send(name.encode(self.FORMAT))
        self.login.destroy()
        self.layout_gui(name)

        rcv = threading.Thread(target=self.receive)
        rcv.start()

    def layout_gui(self, name):
        self.client_name = name

        self.window.deiconify()
        self.window.title("Chat")

        self.window.resizable(width=False,
                              height=False)

        self.window.configure(width=500, height=500, bg="#E2D1F9")
        self.label_name = tk.Label(master=self.window, text=f"You are logged as: {self.client_name}", font=("Aerial", 20), bg="#E2D1F9", fg="#101820")
        self.label_name.place(relheight=0.1,
                              relx=0.15,)

        self.chat_room = tk.Text(self.window, width=16, height=2, bg="#101820", fg="#EAECEE", font=("Aerial", 20))

        self.chat_room.place(relheight=0.7,
                             relwidth=0.90,
                             rely=0.08,
                             relx=0.05)

        self.send_button = tk.Button(master=self.window, text="Send message", font=("Aerial", 20),
                                     command=lambda: self.send_button_f(self.chat.get()))

        self.send_button.place(
            relwidth=1,
            relheight=0.1,
            rely=0.9,
        )

        self.chat_room.config(cursor="arrow")

        self.scrollbar = tk.Scrollbar(master=self.window)

        self.scrollbar.place(relheight=0.65,
                             relx=0.95,
                             rely=0.1)

        self.scrollbar.configure(command=self.chat_room.yview)

        self.chat_room['yscrollcommand'] = self.scrollbar.set

        self.chat_room.config(state=tk.DISABLED)

        self.chat = tk.Entry(master=self.window, font=("Aerial", 20))

        self.chat.place(relwidth=1,
                        relheight=0.12,
                        rely=0.78, )

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode(self.FORMAT)
                self.chat_room.config(state=tk.NORMAL)
                self.chat_room.insert(tk.END, f"\n{message}")
                self.chat_room.config(state=tk.DISABLED)
                self.chat_room.see(tk.END)
            except:
                print("disconnected")
                self.client.close()
                break

    def send_button_f(self, message):
        self.msg = message
        self.chat_room.config(state=tk.DISABLED)
        self.chat.delete(0, tk.END)
        snd = threading.Thread(target=self.send_message())
        snd.start()

    def send_message(self):
        message = self.msg
        self.client.send(message.encode(self.FORMAT))
        if self.msg == "!DISCONNECT":
            self.quit()

    def quit(self):
        self.window.quit()
        quit()


class_gui_client = CLIENT()
