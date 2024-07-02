

#{
# login = bool
# currentUser = array of string
# }

def LOGOUT(currentUser, login):
    if login:
        currentUser.clear()
        login = False
        print("Anda berhasil logout!!")
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    print()

    return login, currentUser

# LOGOUT(currentUser)