

###{KAMUS DATA
# role = str
# oc = int
# monsterAwal = array of string
# validUsername = bool
# notExistUsername = bool
# tempUsername = list of string
# valid = bool
# tempList = array of string
# cnt = int
# username = string
# password = string
# tempUserpasList = array of string
# angkaMonster = int
# monster = string
# tempMInv = array of string}


def isUsernameValid(username): # if the characters are in letters or numbers, the username will be valid
    valid = True
    tempUsername = [char for char in username]
    for i in tempUsername: 
        if (ord(i) >= 0 and ord(i) <= 47 and ord(i) != 45) or (ord(i) > 57 and ord(i) < 65) or (ord(i) > 90 and ord(i) != 95 and ord(i) < 97) or ord(i) > 122:
            valid = False
            break
    return (valid)


def isUsernameExist(username, userpas): # if the username already exist in the database, the username won't be valid
    valid = True
    tempList = []
    for i in range(len(userpas)):
        for j in range(len(userpas)):
            if j == 1:
                tempList.append(userpas[i][j])
    for i in tempList:
        if username == i:
            valid = False
            break
    return (valid)


def REGISTER(userpas, mInv):
    role = 'agent' # starting role
    oc = 0 # starting OC

    monsterAwal = ["Pikachow", "Bulbu", "Zeze", "Zuko", "Chacha"] # starting monsters
    validUsername = True
    notExistUsername = True

    cnt = len(userpas) # number of account

    username = input("Masukkan username: ") 
    password = input("Masukkan password: ")
    print()

    validUsername = isUsernameValid(username) # check username characters validity
    while validUsername == False: # if not valid, repeat the input
        print("Username hanya boleh berisi alfabet, angka, underscore, dan strip")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        validUsername = isUsernameValid(username)

    notExistUsername = isUsernameExist(username, userpas) # check username existence
    while notExistUsername == False: # if not valid, repeat the input
        print(
            f"Username {username} sudah terpakai, silahkan gunakan username lain!")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        notExistUsername = isUsernameExist(username, userpas)

    tempUserpasList = [cnt, username, password, role, oc]
    userpas.append(tempUserpasList) # adding new account to the user database


    print("Silahkan pilih salah satu monster sebagai monster awalmu.")
    print("1. Pikachow")
    print("2. Bulbu")
    print("3. Zeze")
    print("4. Zuko")
    print("5. Chacha")
    print()
    angkaMonster = int(input("Monster pilihanmu: "))
    monster = monsterAwal[angkaMonster-1] # chosen monster

    print(
        f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster}!")

    tempMInv = [int(cnt), int(angkaMonster), 1]
    mInv.append(tempMInv) # adding new monster to monster_inventory database
    cnt += 1 # increase cnt as you add this account

# REGISTER(cnt)