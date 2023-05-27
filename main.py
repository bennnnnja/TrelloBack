import socket
from Parser import handle_client



HOST = '127.0.0.1'
PORT = 65432


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    print(f"server is on {HOST}:{PORT}")   
    print(f"connected: {addr}")


    while True:
        
        command, message = handle_client(conn, addr)


if __name__ == "__main__":
    main()