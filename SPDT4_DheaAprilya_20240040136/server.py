import socket

def server_program():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server berjalan di {host}:{port}, menunggu koneksi...")

    conn, address = server_socket.accept()
    print(f"Koneksi dari: {address}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Pesan diterima oleh server.".encode())

    conn.close()
    print("Koneksi ditutup.")

if __name__ == '__main__':
    server_program()