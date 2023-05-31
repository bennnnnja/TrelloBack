from Database import Database


desks = Database("data/desks.txt")
columns = Database("data/columns.txt")
cards = Database("data/cards.txt")

class User: 

    def __init__(self, login, password):
        self.login = login 
        self.password = password 


    def getInfo(self):
        return str(f"{self.login}:{self.password}")

class Desk: 

    def __init__(self, owner, name, desktype):
        self.name = name 
        self.owner = owner 
        self.desktype = desktype 


    def create(self):        
        desks.write(f"{self.owner}!{self.name}!{self.desktype}")

class Column: 

    def __init__(self, name, owner, desk_id):
        self.name = name 
        self.owner = owner 
        self.desk_id = desk_id 


    def create(self):        
        desks.write(f"{self.owner}!{self.name}!{self.parent}!{self.desk_id}")

class Card: 

    def __init__(self, name, owner, content, column_id):
        self.name = name 
        self.owner = owner 
        self.content = content 
        self.column_id = column_id 


    def create(self):        
        desks.write(f"{self.owner}!{self.name}!{self.content}!{self.column_id}")

