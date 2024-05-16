import os


# Fungsi untuk menyimpan pada CSV terspesifikasi
def save_csv(file_path, df):
    with open(file_path, "w") as file:
        for line in df:
            row = ""
            for i, value in enumerate(line):
                row += str(value)
                if i < len(line) - 1:
                    row += ";"
            row += "\n"
            file.write(row)


# Fungsi untuk memilih list yang sesuai
def list_to_index(
    itemInventory, itemShop, monsterInventory, monsterShop, monster, user, index
):
    if index == 0:
        return itemInventory
    elif index == 1:
        return itemShop
    elif index == 2:
        return monsterInventory
    elif index == 3:
        return monsterShop
    elif index == 4:
        return monster
    elif index == 5:
        return user


# Fungsi utama, simpan kepada direktori terspesifikasi
def save(
    folder_path, itemInventory, itemShop, monsterInventory, monsterShop, monster, user
):
    # folder_path = str(os.getcwd()) + "/" + str(folder_path) # File path fixed
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    csvToSave = [
        "item_inventory.csv",
        "item_shop.csv",
        "monster_inventory.csv",
        "monster_shop.csv",
        "monster.csv",
        "user.csv",
    ]
    for index, file_path in enumerate(csvToSave):
        save_csv(
            folder_path + "/" + file_path,
            list_to_index(
                itemInventory,
                itemShop,
                monsterInventory,
                monsterShop,
                monster,
                user,
                index,
            ),
        )

    print("Segala perubahan telah tersimpan!\n")