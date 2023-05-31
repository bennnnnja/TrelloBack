class Column:
    
    def __init__(self, name, number, cards):
        self.name = name
        self.number = number
        self.cards = cards

    def getInfo(self):
        return str(f"{self.title}!{self.owner}!{self.columns}!{self.is_public}")
