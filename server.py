import socket
import threading
import time


class Server:

    def __init__(self):
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.port = 5050
        self.address = (self.SERVER, self.port)
        self.format = 'utf-8'
        self.clients = {}

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.address)

    def start_app(self):
        print("[SERVER] is starting...")
        time.sleep(1)
        print(f"[SERVER] is hosted on {self.SERVER}")
        self.server.listen()

        while True:
            conn, addr = self.server.accept()

            name = conn.recv(1024).decode(self.format)
            self.clients[conn] = name

            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

    def handle_client(self, conn, addr):
        print(f"[SERVER NOTICE] new connection {self.clients[conn]}\n")
        try:
            connected = True
            while connected:
                message = conn.recv(1024).decode(self.format)
                if message == "!DISCONNECT":
                    message = f"{self.clients[conn]} has been disconnected for the chatroom"
                    for key, value in self.clients.items():
                        key.sendall(message.encode(self.format))
                    print(message)
                    connected = False
                else:
                    if message:
                        message = f"[{self.clients[conn]}]: {message}"
                        for key, value in self.clients.items():
                            key.sendall(message.encode(self.format))
        finally:
            del self.clients[conn]
            conn.close()


Server().start_app()
