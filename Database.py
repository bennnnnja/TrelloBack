class Database: 

    def __init__(self, db_name):
        self.db_name = db_name
        self.db_file = open(db_name, "a+")

    

    def write(self, data):
        new_id = self.get_max_id() + 1
        with open(self.db_name, 'a') as file:
            file.write(f"{new_id}:{data}\n")
            self.db_file.close()


    def searchfor(self, value: str):                
        with open(self.db_name) as f:
                for i in f:
                    if (f"{value}") in i:                       
                        return True, str(i)
                                              
        return False, ""

    def get_max_id(self):
        max_id = 0
        with open(self.db_name, 'r') as file:
            for line in file:
                current_id = int(line.split(':')[0])
                if current_id > max_id:
                    max_id = current_id
        self.db_file.close()            
        return max_id

    

    

    def update(self, key, value, new_data): # возможность обновления
        lines = self.read_all()
        self.db_file.seek(0)
        self.db_file.truncate(0)
        for line in lines:
            if key in line and value in line:
                line = new_data
            self.db_file.write(line)

    def delete(self, key, value): # возможность удаления
        lines = self.read_all()
        self.db_file.seek(0)
        self.db_file.truncate(0)
        for line in lines:
            if not (key in line and value in line):
                self.db_file.write(line)


    def unload_users(self): # выгрузка пользователей с возможность взаимодействия в цикле
        a = ""
        with open(self.db_name, "r") as file:
            for line in file:
                a += str(line) 

        return a
            


    def close(self):
        self.db_file.close()



