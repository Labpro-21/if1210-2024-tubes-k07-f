from src.login import *


def HELP(currentUser):
    print()
    print("=========== HELP ===========")
    if currentUser == []:
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print("   1. Login: Masuk ke dalam akun yang sudah terdaftar")
        print("   2. Register: Membuat akun baru")
        print("   3. Save: ")
        print("   4. Exit: ")
    elif currentUser[3] == 'agent':
        print(
            f"Halo Agent {currentUser[1]}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian.")
        print("Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
        print("   1. Logout: Keluar dari akun yang sedang digunakan")
        print("   2. Monster: Melihat owca-dex yang dimiliki oleh Agent")
        print("   3. Battle: Melawan satu musuh secara random")
        print("   4. Arena: Memasuki arena yang memiliki 5 tingkat, yang mana player akan melawan monster dengan level sesuai tingkat secara melanjut")
        print("   5. Shop: Memasuki tempat membeli monster dan potion")
        print("   6. Laboratory: Memasuki tempat meningkatkan level monster dengan biaya tertentu")
        print("   7. Save: Menyimpan semua progres")
        print("   8. Exit: Keluar dari program")

    elif currentUser[3] == 'admin':
        print("Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:")
        print("   1. Logout: Keluar dari akun yang sedang digunakan")
        print("   2. Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
        print("   3. Monster: Melakukan manajemen monster")
        print("   4. Save: Menyimpan semua progres")
        print("   5. Exit: Keluar dar program")
    print("Footnote :")
    print("   1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
    print("   2. Jangan lupa untuk memasukkan input yang valid")
    print()

# HELP(currentUser)