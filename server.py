import socket
import threading

SERVER = None
IP_ADDRESS = "127.0.0.1"
PORT = 1234
CLIENTS = {}

def setup():
    global SERVER, IP_ADDRESS, PORT
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)

def acceptConnection():
    global SERVER, CLIENTS
    while True:
        client, addr = SERVER.accept()
        CLIENTS[addr] = client
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

def handle_client(client, addr):
    pass

if __name__ == '__main__':
    setup()
    acceptConnection()
