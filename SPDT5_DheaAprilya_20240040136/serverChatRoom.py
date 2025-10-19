import socket
import threading

def broadcast(message, clients, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(conn, addr, clients):
    print(f"Connected by {addr}")
    while True:
        try:
            message = conn.recv(1024)
            if not message:
                break
            broadcast(message, clients, conn)
        except:
            break
    conn.close()
    clients.remove(conn)
    print(f"Connection closed {addr}")

HOST = '127.0.0.1' 
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Server started on {HOST}:{PORT}")

clients = []

while True:
    conn, addr = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr, clients))
    thread.start()