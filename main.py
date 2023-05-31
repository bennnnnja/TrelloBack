import socket
from Parser import handle_client
from Database import Database
from entyties import Desk
from entyties import User


HOST = '127.0.0.1'
PORT = 65432
users = Database("data/users.txt")
desks = Database("data/desks.txt")




def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    print(f"server is on {HOST}:{PORT}")   
    print(f"connected: {addr}")
    current_user="None"

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
            accessed, current_user = users.searchfor(message)
            current_user = current_user.split(":")[0]
            if accessed:
                conn.send(("Accepted!").encode('utf-8'))
            else: 
                
                conn.send(("Declined!").encode('utf-8'))

        if "UnloadData" in command:
            data = ""
            with open("data/desks.txt") as f:
                for i in f:                    
                    if str(i).split(":")[2] =="public\n":
                        data += str(i)
                    elif str(i).split(":")[0] == f"{current_user}":
                        data += str(i)            
            conn.send((f"{data}").encode('utf-8'))

        

        if "NewDesk" in command:
            exists, desk = desks.searchfor(message)
            if not exists:
                desk_name, desk_type = message.split(":")
                new_desk = Desk(current_user.split(":")[0], desk_name, desk_type)
                desks.write(new_desk)
                desks.close()
                conn.send(("Desk created!").encode( 'utf-8'))
            else: conn.send(("Desk exists!").encode( 'utf-8'))

        if "NewJson" in command:
            with open("data/newjson.txt", "a+") as f:
                f.write(message)

        if "UnloadJson" in command:
            data=""
            with open('data/newjson.txt', 'r') as f:
                for i in f:
                    data+=str(i)
            conn.send((f"{data}").encode('utf-8'))

        

            
                

        

        


if __name__ == "__main__":
    main()