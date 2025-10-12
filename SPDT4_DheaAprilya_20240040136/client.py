import socket

def client_program():
    host = input("Masukkan alamat IP server: ")
    port = 12345  

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("Masukkan pesan untuk dikirim ke server: ")

    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()

    print(f"Balasan dari server: {data}")

    client_socket.close()

if __name__ == '__main__':
    client_program()