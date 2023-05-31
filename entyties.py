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

    def __init__(self, name, owner, parent):
        self.name = name 
        self.owner = owner 
        self.parent = parent 


    def create(self):        
        desks.write(f"{self.owner}!{self.name}!{self.parent}")

class Card: 

    def __init__(self, name, owner, content):
        self.name = name 
        self.owner = owner 
        self.content = content 


    def create(self):        
        desks.write(f"{self.owner}!{self.name}!{self.content}")

