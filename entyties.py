from Database import Database

class User: 

    def __init__(self, login, password):
        self.login = login 
        self.password = password 
         

    def getInfo(self):
        return str(f"{self.login}:{self.password}")



class Desk: 

    def __init__(self, name, owner, desktype):
        self.name = name 
        self.owner = owner 
        self.desktype = desktype 
         

    def create(self):
        newdb = Database(f"data/desks/{self.name}.txt")
        newdb.write(f"{self.name}!{self.owner}!{self.desktype}")



