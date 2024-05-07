from src.login import *

def LOGOUT(currentUser):
    if currentUser != []:
        currentUser.clear()
        print("Anda berhasil logout!!")
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    print()

# LOGOUT(currentUser)