import socket
from Parser import handle_client
from Database import Database
from entyties import Desk
from entyties import User



HOST = '127.0.0.1'
PORT = 65432
database = Database("users.txt")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    print(f"server is on {HOST}:{PORT}")   
    print(f"connected: {addr}")

    while True:
        
        command, message = handle_client(conn, addr)

        if "NewUser" in command:
            exists, user = database.searchfor(message)
            if not exists:
                login, password = message.split(":")
                new_user = User(login, password)
                database.write(new_user)
                database.close()
                conn.send(("Account created!").encode( 'utf-8'))
            else: conn.send(("Account exists!").encode( 'utf-8'))

        if "Entrance" in command:
            accessed, user = database.searchfor(message)
            if accessed:
                conn.send(("Accepted!").encode('utf-8'))
            else: 
                
                conn.send(("Declined!").encode('utf-8'))

        if "UnloadUsers" in command:

            UnUsers = database.unload_users()
            conn.send((f"{UnUsers}").encode('utf-8'))


if __name__ == "__main__":
    main()