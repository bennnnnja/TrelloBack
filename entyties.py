
class User: 

    def __init__(self, login, password):
        self.login = login 
        self.password = password 


    def getInfo(self):
        return str(f"{self.login}:{self.password}")

class Desk:
    def __init__(self, owner, desk_name, desk_type):
        self.owner = owner 
        self.desk_name = desk_name 
        self.desk_type = desk_type 

    def getInfo(self):
        return str(f"{self.owner}:{self.desk_name}:{self.desk_type}")