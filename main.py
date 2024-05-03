# TUBES DASPRO ----------------------------------------------------------------------------------
import os
import sys
import time
import math
import argparse
import datetime

# lINEAR CONGRUENTIAL GENERATOR (RNG) ----------------------------------------------------------------------------------
# def seedLCG(initVal):
#     global rand
#     rand = initVal

# def lcg():
#     a = 1140671485
#     c = 128201163
#     m = 2**24
#     global rand
#     rand = (a*rand + c) % m
#     return rand

# seedLCG(5)

# # int(os.getpid() + time.time())

# for i in range(10):
#     print(lcg())

# COLOR (buat warnain doang :v) ----------------------------------------------------------------------------------
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Contoh : print(color.BOLD + 'Hello, World!' + color.END)

# REGISTER
def read_csv(file_path):
    data = []
    row = []
    field = ""
    in_quotes = False

    with open(file_path, 'r') as file:
        for char in file.read():
            if char == ';' and not in_quotes:
                char = ','
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

def isUsernameValid(username):
    valid = True
    tempUsername = [char for char in username]
    for i in tempUsername:
        if (ord(i) >= 0 and ord(i) <= 47 and ord(i) != 45) or (ord(i) > 57 and ord(i) < 65) or (ord(i) > 90 and ord(i) != 95 and ord(i) < 97) or ord(i) > 122:
            valid = False
            break
    return (valid)

def isUsernameExist(username, userpas):
    validity = True
    tempList = []
    for i in range(len(userpas)):
        for j in range(len(userpas)):
            if j == 1:
                tempList.append(userpas[i][j])
    print(tempList)
    for i in tempList:
        if username == i:
            validity = False
            break
    return (validity)

def Register(cnt):
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
    print (notExistUsername)
    while notExistUsername == False:
        print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        notExistUsername = isUsernameExist(username, userpas)

    # ini temporary, ntar pas save lgsg ngewrite ke csv
    tempUserpasList = []
    tempUserpas = str(cnt)+";"+username+";"+password+";"+role+";"+str(oc)
    tempUserpasList.append(tempUserpas)

    # f = open('user.csv', 'a')
    # acc = str(cnt+1)+";"+username+";"+password+";"+role+";"+str(oc)
    # f.write("\n"+acc)
    # f.close()

    print("Silahkan pilih salah satu monster sebagai monster awalmu.")
    print("1. Pikachow")
    print("2. Bulbu")
    print("3. Zeze")
    print("4. Zuko")
    print("3. Chacha")
    print()
    angkaMonster = int(input("Monster pilihanmu: "))
    monster = monsterAwal[angkaMonster-1]

    print(
        f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster}!")

# LOGIN ----------------------------------------------------------------------------------
# loginBool = False
# wrongUsername = False
# wrongPassword = False
# alreadyLogin = False


def isPasswordCorrect(loginUsername, loginPassword, userList, passList):
    Bool = False
    for i in range(len(userList)):
        if loginUsername == userList[i] and loginPassword != passList[i]:
            Bool = True
    return (Bool)


def isLoginValid(loginUsername, loginPassword, userList, passList):
    Bool = False
    for i in range(len(userList)):
        if loginUsername == userList[i] and loginPassword == passList[i]:
            Bool = True
    return (Bool)


def isUsernameExist(wrongPassword, loginBool):
    Bool = False
    if wrongPassword == False and loginBool == False:
        Bool = True
    return (Bool)


def Login(loginBool, wrongUsername, wrongPassword, alreadyLogin, userpas):
    if loginBool:
        print(f"Selamat datang, Agent {loginUsername}!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
    elif wrongUsername:
        print("Username tidak terdaftar!")
    elif wrongPassword:
        print("Password salah!")
    print()

# LOGOUT
# def Logout(alreadyLogin, currentUser):
#     if alreadyLogin:
#         currentUser.clear()
#         alreadyLogin = False
#         return (alreadyLogin)
#     else:
#         print("Logout gagal!")
#         print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")


# HELP
def Help(alreadyLogin, currentUser):
    print()
    print("=========== HELP ===========")
    if not alreadyLogin:
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print("   1. Login: Masuk ke dalam akun yang sudah terdaftar")
        print("   2. Register: Membuat akun baru")
    elif alreadyLogin and currentUser[2] == 'agent':
        print(
            f"Halo Agent {currentUser[0]}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian.")
        print("Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
        print("   1. Logout: Keluar dari akun yang sedang digunakan")
        print("   2. Monster: Melihat owca-dex yang dimiliki oleh Agent")
        print("   3. Tambah lagi ntar")
    elif alreadyLogin and currentUser[2] == 'admin':
        print("Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:")
        print("   1. Logout: Keluar dari akun yang sedang digunakan")
        print("   2. Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
        print("   3. Tambah lagi ntar")
    print("Footnote :")
    print("   1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
    print("   2. Jangan lupa untuk memasukkan input yang valid")
    print()

# INVENTORY
def Inventory(currentUser, mInv, iInv, mons):
    print(f"============ INVENTORY LIST (User ID: {currentUser[0]}) ============")
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {currentUser[4]}")
    invCount = 0
    mTemp = []
    iTemp = []


    for i in range(len(mInv)):
        if mInv[i][0] == str(currentUser[0]):
            print(
                f"{invCount+1}. Monster       (Name: {mons[i][1]}, Lvl: {mInv[i][2]}, HP: {mons[i][4]})")
            invCount += 1
            stats = [invCount, mons[i][1], mons[i][2],
                    mons[i][3], mons[i][4], mInv[i][2]]
            mTemp.append(stats)

    for i in range(len(iInv)):
        if iInv[i][0] == str(currentUser[0]):
            print(
                f"{invCount+1}. Potion        (Type: {iInv[i][1]}, Qty: {iInv[i][2]})")
            invCount += 1
            potInfo = [invCount, iInv[i][1], iInv[i][2]]
            iTemp.append(potInfo)

    print()
    while True:
        pilihanInv = input(">>> ")
        if pilihanInv.upper() != "KELUAR":
            if int(pilihanInv) <= int(len(mTemp)):
                for i in range(len(mTemp)):
                    if int(pilihanInv) == mTemp[i][0]:
                        print("Monster")
                        print(f"Name      : {mTemp[i][1]}")
                        print(f"ATK Power : {mTemp[i][2]}")
                        print(f"Def Power : {mTemp[i][3]}")
                        print(f"HP        : {mTemp[i][4]}")
                        print(f"Level     : {mTemp[i][5]}")
                        print()
                        break
            elif int(pilihanInv) > int(len(mTemp)):
                for i in range(len(iTemp)):
                    if int(pilihanInv) == iTemp[i][0]:
                        print("Potion")
                        print(f"Type      : {iTemp[i][1]}")
                        print(f"Quantity  : {iTemp[i][2]}")
                        print()
                        break
        elif pilihanInv.upper() == "KELUAR":
            print()
            break
        else:
            if invCount == 1:
                print("Pilihan hanyalah 1 dan 'KELUAR'")
            else:
                print(f"Pilihan hanyalah 1-{invCount} dan 'KELUAR'")
            print()

    

# MONSTER
# print("                              __")
# print("                            .d$$b")
# print("                          .' TO$;'")
# print("                         /  : TP._;")
# print("                        / _.;  :Tb|")
# print("                       /   /   ;j$j")
# print("                   _.-'       d$$$$")
# print("                 .' ..       d$$$$;")
# print("                /  /P'      d$$$$P. |'")
# print("               /   "      ".d$$$P |\^")
# print("             .'           `T$P^""   :;")
# print("         ._.'      _.'              ;;")
# print("      `-.-.-'-' ._.       _.-    .-")
# print("    `.-' _____  ._   '           .-")
# print("   -(.g$$$$$$$b.              .'")
# print("     ""^^T$$$P^)            .(:")
# print("       _/  -"  '         /:/;'"")
# print("    ._.'-'`-'  /         /;/;'")
# print(" `-.-'..--''   '' /         /  ;")
# print(".-' ..--'       -'          :")
# print("..--'--.-''                 :")
# print("  ..--""              `-\(\/;`")
# print("    _.                      :")
# print("                            ;`-")


# VARIABEL (KAMUS) ----------------------------------------------------------------------------------
userpas = read_csv('user.csv')
mInv = read_csv('monster_inventory.csv')
iInv = read_csv('item_inventory.csv')
mons = read_csv('monster.csv')

cnt = len(userpas)
monsterAwal = ["Pikachow", "Bulbu", "Zeze", "Zuko", "Chacha"]
validUsername = True
notExistUsername = True

currentUser = []
loginBool = False
wrongUsername = False
wrongPassword = False
alreadyLogin = False
tempLogin = False

# ALGORITMA PROGRAM UTAMA ----------------------------------------------------------------------------------

print("SELAMAT DATANG PADA PROGRAM YANG SEDANG DALAM PERCOBAAN INI!!!")
while True:
    pilihan = input(">>> ")
    if pilihan.upper() == "REGISTER": #REGISTER -----------------------------------------------------------------------
        Register(cnt)
        cnt += 1
    if pilihan.upper() == "LOGIN": #LOGIN -----------------------------------------------------------------------
        if alreadyLogin:
            print("Login gagal!")
            print(f"Anda telah login dengan username {currentUser[1]}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.")
        else:
            loginUsername = input("Masukkan username : ")
            loginPassword = input("Masukkan password : ")
            userList = []
            passList = []
            for i in range(len(userpas)):
                for j in range(len(userpas)):
                    if j == 1:
                        userList.append(userpas[i][j])
            for i in range(len(userpas)):
                for j in range(len(userpas)):
                    if j == 2:
                        passList.append(userpas[i][j])

            wrongPassword = isPasswordCorrect(loginUsername, loginPassword, userList, passList)
            loginBool = isLoginValid(loginUsername, loginPassword, userList, passList)
            wrongUsername = isUsernameExist(wrongPassword, loginBool)

            Login(loginBool, wrongUsername,wrongPassword, alreadyLogin, userpas)
            alreadyLogin = isLoginValid(loginUsername, loginPassword, userList, passList)

            for i in range(len(userList)):
                for j in range(len(userList)):
                    if userList[i] == loginUsername:
                        currentUser.append(int(userpas[i][0])) # userid
                        currentUser.append(userpas[i][1]) # username
                        currentUser.append(userpas[i][2]) # password
                        currentUser.append(userpas[i][3]) # role
                        currentUser.append(int(userpas[i][4])) # oc
                        break
            print (currentUser) #buat ngetes

    if pilihan.upper() == "LOGOUT": #LOGOUT -----------------------------------------------------------------------
        if alreadyLogin:
            currentUser.clear()
            alreadyLogin = False
            print("Anda berhasil logout!!")
        else:
            print("Logout gagal!")
            print(
                "Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        print()

    if pilihan.upper() == "HELP": #HELP -----------------------------------------------------------------------
        Help(alreadyLogin, currentUser)

    if pilihan.upper() == "INVENTORY": #INVENTORY -----------------------------------------------------------------------
        Inventory(currentUser, mInv, iInv, mons)

    if pilihan.upper() == "EXIT": #EXIT
        break


