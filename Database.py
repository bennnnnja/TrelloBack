from entyties import User

class Database: 

    def __init__(self, db_name):
        self.db_name = db_name
        self.db_file = open(db_name, "a+")

    

    def write(self, user: User): # возможность записи
        self.db_file = open(self.db_name, "a+")
        self.db_file.write(user.getInfo()) 
        self.db_file.write("\n")
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
   


    def unload_data(self): # выгрузка пользователей с возможность взаимодействия в цикле
        a = ""
        with open(self.db_name, "r") as file:
            for line in file:
                a += str(line) 

        return a
            


    def close(self):
        self.db_file.close()

def swap_lines(file_path, line1, line2):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            print(lines)
            f.close()
        id1, data1 = lines[line1-1].split(':', 1)
        id2, data2 = lines[line2-1].split(':', 1)
        lines[line1-1] = f"{id1}:{data2}"
        lines[line2-1] = f"{id2}:{data1}"
        with open(file_path, 'w') as f:
            f.writelines(lines)
            f.close()



