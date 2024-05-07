import os
from src.csv import *

monsterAwal = ["Pikachow", "Bulbu", "Zeze", "Zuko", "Chacha"]
validUsername = True
notExistUsername = True

userpas = read_csv(user_filepath())
mInv = read_csv(monster_inventory_filepath())
cnt = len(userpas)


def isUsernameValid(username):
    valid = True
    tempUsername = [char for char in username]
    for i in tempUsername:
        if (ord(i) >= 0 and ord(i) <= 47 and ord(i) != 45) or (ord(i) > 57 and ord(i) < 65) or (ord(i) > 90 and ord(i) != 95 and ord(i) < 97) or ord(i) > 122:
            valid = False
            break
    return (valid)


def isUsernameExist(username, userpas):
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


def REGISTER(cnt):
    role = 'agent'
    oc = 0

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    print()

    validUsername = isUsernameValid(username)
    while validUsername == False:
        print("Username hanya boleh berisi alfabet, angka, underscore, dan strip")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        validUsername = isUsernameValid(username)

    notExistUsername = isUsernameExist(username, userpas)
    while notExistUsername == False:
        print(
            f"Username {username} sudah terpakai, silahkan gunakan username lain!")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        notExistUsername = isUsernameExist(username, userpas)

    # ini temporary, ntar pas save lgsg ngewrite ke csv
    cnt = len(userpas)
    tempUserpasList = []
    tempUserpas = str(cnt)+";"+username+";"+password+";"+role+";"+str(oc)
    tempUserpasList.append(cnt)
    tempUserpasList.append(username)
    tempUserpasList.append(password)
    tempUserpasList.append(role)
    tempUserpasList.append(oc)
    userpas.append(tempUserpasList)

    # Buat save nanti ?
    # f = open('user.csv', 'a')
    # for i in tempUserpasList:
    #   f.write("\n"+i)
    # f.close()

    print("Silahkan pilih salah satu monster sebagai monster awalmu.")
    print("1. Pikachow")
    print("2. Bulbu")
    print("3. Zeze")
    print("4. Zuko")
    print("5. Chacha")
    print()
    angkaMonster = int(input("Monster pilihanmu: "))
    monster = monsterAwal[angkaMonster-1]

    print(
        f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster}!")

    tempMInv = []
    tempMInv.append(int(cnt))
    tempMInv.append(int(angkaMonster))
    tempMInv.append(1)
    mInv.append(tempMInv)
    cnt += 1

    return(userpas)

# REGISTER(cnt)