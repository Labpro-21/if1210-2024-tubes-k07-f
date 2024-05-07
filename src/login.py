from src.csv import *
from src.register import *

currentUser = []
loginBool = False
wrongUsername = False
wrongPassword = False


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


def LOGIN(loginBool, wrongUsername, wrongPassword, userpas):
    print (userpas)
    if currentUser != []:
        print("Login gagal!")
        print(
            f"Anda telah login dengan username {currentUser[1]}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.")
        print()
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

        wrongPassword = isPasswordCorrect(
            loginUsername, loginPassword, userList, passList)
        loginBool = isLoginValid(
            loginUsername, loginPassword, userList, passList)
        wrongUsername = isUsernameExist(wrongPassword, loginBool)

        if loginBool:
            for i in range(len(userList)):
                for j in range(len(userList)):
                    if userList[i] == loginUsername:
                        currentUser.append(int(userpas[i][0]))  # userid
                        currentUser.append(userpas[i][1])  # username
                        currentUser.append(userpas[i][2])  # password
                        currentUser.append(userpas[i][3])  # role
                        currentUser.append(int(userpas[i][4]))  # oc
                        break
    if loginBool:
        if currentUser[3] == "agent":
            print(f"Selamat datang, Agent {loginUsername}!")
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        elif currentUser[3] == "admin":
            print("Selamat datang, admin")
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
    elif wrongUsername:
        print("Username tidak terdaftar!")
    elif wrongPassword:
        print("Password salah!")
    print()


# LOGIN(loginBool, wrongUsername, wrongPassword, userpas)
