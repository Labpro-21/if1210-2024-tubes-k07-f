# IF1210 - Dasar Pemrograman 2024
> Tugas Besar - IF1210 Dasar Pemrograman 2024

# About
Misi Agent P dan Tim O.W.C.A.

Dalam game ini, pemain bergabung dengan Purry si Platypus, juga dikenal sebagai Agent P, untuk menghadapi ancaman dari Dr. Asep Spakbor yang telah menciptakan monster-monster berbahaya. Pemain harus bekerja sama dengan tim O.W.C.A. untuk menyusun strategi yang matang dan melatih monster-monster yang akan digunakan dalam pertempuran.

Petualangan dimulai dengan misi pencarian monster di hutan terpencil yang diyakini menjadi tempat tinggal bagi berbagai jenis monster. Sepanjang perjalanan, pemain akan diuji keberanian dan ketangkasannya, serta harus siap menghadapi berbagai tantangan yang muncul demi menyelamatkan kota Danville.

Pemain akan:

1. Merencanakan strategi pertempuran bersama tim.
2. Menangkap dan melatih monster.
3. Menghadapi dan mengalahkan monster-monster kuat Dr. Asep Spakbor.

Dengan kerja tim dan tekad yang kuat, pemain akan berusaha mengembalikan keamanan kota Danville dalam game petualangan penuh tantangan ini.

# Contributors
1. Theo Kurniady			19623077
2. Muhammad Fithra Rizki		19623057
3. Gabriela Jennifer Sandy 		19623097
4. Ramadhan Abhinawa Herawanto	16523207
5. Kennard Hezekiah Montoya		16523057


# Features
1. Register
2. Login
3. Logout
4. Help
5. Inventory
6. Battle (+ monster ball)
7. Arena
8. Laboratory
9. Monster Management
10. Shop and Currency
11. Shop Management
12. Save
13. Load
14. Exit

# How to Run
Untuk memulai program, ketik "python main.py nama_folder" dengan keterangan nama_folder adalah nama folder yang berisi 6 CSV save file.
Pada program terdapat . perintah yang berbeda yang bisa dilakukan. Perintah tersebut adalah sebagai berikut:
1. REGISTER
2. LOGIN
3. LOGOUT
4. HELP
5. INVENTORY
6. BATTLE
7. ARENA
8. LABORATORY
9. MONSTER (Admin)
10. SHOP (Admin and Agent)
11. SAVE
12. EXIT

Berikut adalah penjelasan setiap perintah:
1. REGISTER: 
Pada register, pemain memasukkan username dan password baru untuk membuat akun baru. Bila akun tersebut masih baru dan menggunakan karakter yang valid, pemain dapat memilih satu monster untuk menjadi monster awal.

2. LOGIN: 
Pada login, pemain memasukkan username dan password dari akun yang sudah terdaftar. Bila username dan password sesuai, pemain berhasil login dan menggunakan akun tersebut sampai logout atau keluar game.

3. LOGOUT: 
Pada logout, pemain akan keluar dari akun yang sedang digunakan. Logout tidak bisa digunakan bila pemain tidak login terlebih dahulu.

4. HELP: 
Pada help, pemain bisa mendapatkan informasi perintah yang dapat dilakukan tergantung role (admin atau agent). Bila belum memiliki role, help juga menampilkan perintah yang dapat dilakukan pemain.

5. INVENTORY: 
Pada inventory, pemain dapat melihat seluruh barang yang dimilikinya, yaitu OC, monster dan item (potion dan monster ball). Pemain juga dapat melihat setiap barang dengan lebih detail.

6. BATTLE: 
Pada battle, pemain akan melawan monster secara random (tipe dan levelnya). Pemain akan memilih salah satu monster yang dimilikinya untuk melawan monster lawan. Setelah itu, Pemain bisa melakukan 4 perintah, yaitu attack, use potion, use monster ball, dan juga flee. Pada attack, monster pemain akan menyerang terlebih dahulu dan jumlah attack adalah attack yang ditambahkan sesuai level dalam rentang -30% sampai 30% dikurangi dengan defense musuh dalam %. Pada use potion, pemain bisa memakai potion yang dimilikinya (strength, resilience, healing), dimana strength menambah attack sebesar 5%, resilience menambah defense sebesar 5%, dan healing menambah darah sebesar 25%. Pada use monster ball, pemain dapat menangkap monster dengan kesempatan sesuai levelnya (semakin tinggi semakin sulit). Pada flee, pemain bisa langsung kabur dari battle. Bila pemain menang, pemain akan mendapatkan hadiah OC. Bila pemain kalah, pemain tidak akan mendapatkan apapun.

7. ARENA: 
Pada arena, akan ada 5 stage. Pada setiap stage, pemain akan melakukan battle dengan monster yang tipenya random dengan level yang meningkat sesuai nomor stage. Sistem battle pada arena sama seperti BATTLE, hanya saja pemain tidak dapat menangkap monster pada arena. Pemain bisa keluar dari arena di tengah stage dan masih mendapatkan hadiah per stage yang diclear.

8. LABORATORY: 
Pada laboratory, pemain dapat upgrade monster yang dimilikinya dengan harga yang meningkat sesuai dengan levelnya. Bila level sudah maks, monster tidak akan bisa diupgrade lagi.

9. MONSTER: 
Hanya admin yang bisa mengakses perintah ini. Pada monster, admin dapat memanage monster yang ada pada game dengan menambahkan monster disertai attack, def (maks 50), dan hp.

10. SHOP: 
Bila shop diakses admin, admin dapat melakukan shop management. Pada shop management, admin dapat menambahkan monster/item yang belum ada pada shop, mengubah harga dan/atau stok dari monster/item, dan juga menghapus monster/item yang sudah ada di shop. Bila shop diakses agent, agent dapat membeli monster atau potion yang sudah ada di shop. Setiap barang memiliki harga dan dapat dibeli bila stoknya mencukupi.

11. SAVE: 
Pada save, pemain bisa melakukan save dari semua progres yang telah dilakukan. Bila belum ada folder sesuai nama yang di input, folder tersebut akan dibuat.
Bila sudah ada foldernya, data pada folder akan dioverwrite dengan progres

12. EXIT: 
Pada exit, pemain dapat keluar dari game dengan peringatan untuk save.
