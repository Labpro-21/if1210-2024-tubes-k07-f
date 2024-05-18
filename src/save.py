import os
from time import sleep

def write_csv(folder_path, csv_file, array_data):
    # Membuka file csv
    with open(os.path.join(folder_path, csv_file), "w", newline="") as file:
        for i in range(len(array_data)):
            line = ""
            for j in range(len(array_data[i])):
                line += str(array_data[i][j])
                if j < len(array_data[i])-1:
                    line += ";"
                else:
                    line += "\n"
            file.write(line)


def save_data():
    folder_name = input("Masukkan nama folder : ")
    folder_path = os.path.join("./data", folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Membuat folder {folder_path}...")
        sleep (1.5)
        # Pembuatan folder baru karena nama folder belum ditemukan
    
    else :
        print(f"Folder {folder_path} sudah ada.")

    data_user = "Data user.csv"
    data_monster = "Data monster.csv"
    data_item_inventory = "Data item_inventory.csv"
    data_monster_inventory = "Data monster_inventory.csv"
    data_item_shop = "Data item_shop.csv"
    data_monster_shop = "Data monster_shop.csv" 
    
    # Memanggil fungsi untuk menyimpan data ke
    save_file(folder_path, "user.csv", data_user)
    save_file(folder_path, "monster.csv", data_monster)
    save_file(folder_path, "item_inventory.csv", data_item_inventory)
    save_file(folder_path, "monster_inventory.csv", data_monster_inventory)
    save_file(folder_path, "item_shop.csv", data_item_shop)
    save_file(folder_path, "monster_shop.csv", data_monster_shop)

def save_file(folder_path, file_name, data):
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as file:
        file.write(data)

save_data()