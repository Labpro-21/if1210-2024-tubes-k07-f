import os

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        row = []
        field = ""
        in_quotes = False

        for char in file.read():
            if char == ';' and not in_quotes:
                row.append(field)
                field = ""
            elif char == '"' and not in_quotes:
                in_quotes = True
            elif char == '"' and in_quotes:
                in_quotes = False
            elif char == '\n' and not in_quotes:
                row.append(field)
                data.append(row)
                row = []
                field = ""
            else:
                field += char

        if field:
            row.append(field)
            data.append(row)

    return data


def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))


def user_filepath():
    tempFilepath = get_current_directory()
    charFilepath = [char for char in tempFilepath]
    newcharFilepath = []

    if charFilepath[-1] == "c" and charFilepath[-2] == "r" and charFilepath[-3] == "s" and charFilepath[-4] == "\\":
        for i in range(len(charFilepath)-4):
            if ord(charFilepath[i]) != 92:
                newcharFilepath.append(charFilepath[i])
            else:
                newcharFilepath.append("/")
    else:
        for i in (charFilepath):
            if ord(i) != 92:
                newcharFilepath.append(i)
            else:
                newcharFilepath.append("/")

    filepath = ("".join(map(str, newcharFilepath)))
    file_path = filepath+"/data/user.csv"
    return file_path


def monster_filepath():
    tempFilepath = get_current_directory()
    charFilepath = [char for char in tempFilepath]
    newcharFilepath = []

    if charFilepath[-1] == "c" and charFilepath[-2] == "r" and charFilepath[-3] == "s" and charFilepath[-4] == "\\":
        for i in range(len(charFilepath)-4):
            if ord(charFilepath[i]) != 92:
                newcharFilepath.append(charFilepath[i])
            else:
                newcharFilepath.append("/")
    else:
        for i in (charFilepath):
            if ord(i) != 92:
                newcharFilepath.append(i)
            else:
                newcharFilepath.append("/")

    filepath = ("".join(map(str, newcharFilepath)))
    file_path = filepath+"/data/monster.csv"
    return file_path


def monster_shop_filepath():
    tempFilepath = get_current_directory()
    charFilepath = [char for char in tempFilepath]
    newcharFilepath = []

    if charFilepath[-1] == "c" and charFilepath[-2] == "r" and charFilepath[-3] == "s" and charFilepath[-4] == "\\":
        for i in range(len(charFilepath)-4):
            if ord(charFilepath[i]) != 92:
                newcharFilepath.append(charFilepath[i])
            else:
                newcharFilepath.append("/")
    else:
        for i in (charFilepath):
            if ord(i) != 92:
                newcharFilepath.append(i)
            else:
                newcharFilepath.append("/")

    filepath = ("".join(map(str, newcharFilepath)))
    file_path = filepath+"/data/monster_shop.csv"
    return file_path


def monster_inventory_filepath():
    tempFilepath = get_current_directory()
    charFilepath = [char for char in tempFilepath]
    newcharFilepath = []

    if charFilepath[-1] == "c" and charFilepath[-2] == "r" and charFilepath[-3] == "s" and charFilepath[-4] == "\\":
        for i in range(len(charFilepath)-4):
            if ord(charFilepath[i]) != 92:
                newcharFilepath.append(charFilepath[i])
            else:
                newcharFilepath.append("/")
    else:
        for i in (charFilepath):
            if ord(i) != 92:
                newcharFilepath.append(i)
            else:
                newcharFilepath.append("/")

    filepath = ("".join(map(str, newcharFilepath)))
    file_path = filepath+"/data/monster_inventory.csv"
    return file_path


def item_shop_filepath():
    tempFilepath = get_current_directory()
    charFilepath = [char for char in tempFilepath]
    newcharFilepath = []

    if charFilepath[-1] == "c" and charFilepath[-2] == "r" and charFilepath[-3] == "s" and charFilepath[-4] == "\\":
        for i in range(len(charFilepath)-4):
            if ord(charFilepath[i]) != 92:
                newcharFilepath.append(charFilepath[i])
            else:
                newcharFilepath.append("/")
    else:
        for i in (charFilepath):
            if ord(i) != 92:
                newcharFilepath.append(i)
            else:
                newcharFilepath.append("/")

    filepath = ("".join(map(str, newcharFilepath)))
    file_path = filepath+"/data/item_shop.csv"
    return file_path


def item_inventory_filepath():
    tempFilepath = get_current_directory()
    charFilepath = [char for char in tempFilepath]
    newcharFilepath = []

    if charFilepath[-1] == "c" and charFilepath[-2] == "r" and charFilepath[-3] == "s" and charFilepath[-4] == "\\":
        for i in range(len(charFilepath)-4):
            if ord(charFilepath[i]) != 92:
                newcharFilepath.append(charFilepath[i])
            else:
                newcharFilepath.append("/")
    else:
        for i in (charFilepath):
            if ord(i) != 92:
                newcharFilepath.append(i)
            else:
                newcharFilepath.append("/")

    filepath = ("".join(map(str, newcharFilepath)))
    file_path = filepath+"/data/item_inventory.csv"
    return file_path

# userpas = read_csv(user_filepath())
# mons = read_csv(monster_filepath())
# mShop = read_csv(monster_shop_filepath())
# mInv = read_csv(monster_inventory_filepath())
# iShop = read_csv(item_shop_filepath())
# iInv = read_csv(item_inventory_filepath())