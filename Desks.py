class Desks:

    def __init__(self, name, owner, columns, is_public):

        self.name = name
        self.owner = owner
        self.columns = columns
        self.is_public = is_public
    
    def getInfo(self):
        return str(f"{self.name}!{self.owner}!{self.columns}!{self.is_public}")

    