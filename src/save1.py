import os

class Game:
    def __init__(self):
        self.users_file = "users.csv"
        self.monster_inventory_file = "monster_inventory.csv"
        self.item_inventory_file = "item_inventory.csv"
        self.monster_shop_file = "monster_shop.csv"
        self.item_shop_file = "item_shop.csv"
        self.koin_file = "koin.csv"

    def save_data(self, file_path, data):
        folder = os.path.dirname(file_path)
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Membuat folder {folder}...")
        
        with open(file_path, 'w') as file:
            for row in data:
                file.write(','.join(row) + '\n')
        print(f"Berhasil menyimpan data di {file_path}!")

    def register(self, username, password, koin):
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as file:
                for line in file:
                    if line.split(',')[0] == username:
                        print("Username sudah terdaftar!")
                        return False

        with open(self.users_file, 'a') as file:
            file.write(f"{username},{password}\n")


        self.save_data(self.koin_file, [[username, koin]])
        return True

    def login(self, username, password):

        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as file:
                for line in file:
                    user, passwd = line.strip().split(',')
                    if user == username and passwd == password:
                        print("Login berhasil!")
                        return True
        print("Username atau password salah!")
        return False

    def logout(self):
        print("Logout berhasil!")
    def buy_monster(self, monster_name, quantity):
        pass
    def buy_item(self, item_name, quantity):
        pass
