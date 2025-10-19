import socket
import threading
import sys

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if not message:
                print("Disconnected from server")
                break
            print(message)
        except:
            print("Error receiving message")
            break
    sock.close()
    sys.exit()

def send_messages(sock):
    while True:
        try:
            message = input()
            sock.send(message.encode('utf-8'))
        except:
            print("Error sending message")
            sock.close()
            break

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((HOST, PORT))
except:
    print("Unable to connect to server")
    sys.exit()

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

send_thread = threading.Thread(target=send_messages, args=(client_socket,))
send_thread.start()