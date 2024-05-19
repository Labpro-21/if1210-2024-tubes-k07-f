
# {KAMUS
# Bool = bool
# currentUser = array of string
# loginBool = bool
# wrongUsername = bool
# wrongPassword = bool
# loginUsername = string
# loginPassword = string
# userList = array of string
# passList = array of string
# }

def isPasswordCorrect(loginUsername, loginPassword, userList, passList): # check if the password is of the login username
    Bool = False
    for i in range(len(userList)):
        if loginUsername == userList[i] and loginPassword != passList[i]:
            Bool = True
    return (Bool)


def isLoginValid(loginUsername, loginPassword, userList, passList): # check login validity
    Bool = False
    for i in range(len(userList)):
        if loginUsername == userList[i] and loginPassword == passList[i]:
            Bool = True
    return (Bool)


def isUsernameExist(wrongPassword, loginBool): # check username existence
    Bool = False
    if wrongPassword == False and loginBool == False:
        Bool = True
    return (Bool)


def LOGIN(userpas):
    currentUser = []
    loginBool = False
    wrongUsername = False
    wrongPassword = False

    loginUsername = input("Masukkan username : ")
    loginPassword = input("Masukkan password : ")
    userList = []
    passList = []
    for i in range(len(userpas)): # making an array of usernames
        for j in range(len(userpas)):
            if j == 1:
                userList.append(userpas[i][j])
    for i in range(len(userpas)): # making an array of passwords
        for j in range(len(userpas)):
            if j == 2:
                passList.append(userpas[i][j])

    wrongPassword = isPasswordCorrect(loginUsername, loginPassword, userList, passList) 
    loginBool = isLoginValid(loginUsername, loginPassword, userList, passList)
    wrongUsername = isUsernameExist(wrongPassword, loginBool)

    if loginBool: # if successfully login
        for i in range(len(userList)):
            for j in range(len(userList)):
                if userList[i] == loginUsername:
                    currentUser.append(int(userpas[i][0]))  # userid
                    currentUser.append(userpas[i][1])  # username
                    currentUser.append(userpas[i][2])  # password
                    currentUser.append(userpas[i][3])  # role
                    currentUser.append(int(userpas[i][4]))  # oc
                    break

        if currentUser[3] == "agent": # if role is agent
            print(f"Selamat datang, Agent {loginUsername}!")
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        elif currentUser[3] == "admin": # if role is admin
            print("Selamat datang, admin")
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
    elif wrongUsername: # if username doesn't exist
        print("Username tidak terdaftar!")
        loginBool = False
    elif wrongPassword: # if the password is not the one listed with the username
        print("Password salah!")
        loginBool = False
    print() 
    return loginBool, currentUser

# LOGIN(loginBool, wrongUsername, wrongPassword, userpas)
