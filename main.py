import socket
from Parser import handle_client
from Database import Database
from entyties import Desk
from entyties import User



HOST = '127.0.0.1'
PORT = 65432
users = Database("data/users.txt")

user = "begula:12345678"

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
            exists, user = users.searchfor(message)
            if not exists:
                login, password = message.split(":")
                new_user = User(login, password)
                users.write(new_user)
                users.close()
                conn.send(("Account created!").encode( 'utf-8'))
            else: conn.send(("Account exists!").encode( 'utf-8'))

        if "Entrance" in command:
            accessed, user = users.searchfor(message)
            if accessed:
                conn.send(("Accepted!").encode('utf-8'))
            else: 
                
                conn.send(("Declined!").encode('utf-8'))

        if "NewDesk" in command: 
            user = "begula:12345678"
            name, desktype = message.split("!")
            new_desk = Desk(name, user.split(":")[0], desktype)
            new_desk.create() 

        if "AddColumn" in command:            
            desk, column = message.split("!")
            
                

        

        


if __name__ == "__main__":
    main()