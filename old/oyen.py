import random

nama = "Bintang Novian"
umur = 17

oyen_position = random.randint(1, 5)

print("**********************")
print(f"*** {nama} ***")
print(f"********* {umur} *********")
print("**********************")

nama_user = input("Coba Masukkan Nama Kamu : ")
# print(nama_user)

print(f'''Halo {nama_user}!
      Coba Perhatikan Goa Dibawah Ini
      |_| |_| |_| |_| |_|
      ''')

pilihan_user = int(input("Menurut kamu, di goa nomor berapakah oyen berada? [1, 2, 3, 4, 5] "))
# print(f"Pilihan kamu adalah {pilihan_user}")

user_yakin = input("Apakah kamu sudah yakin dengan pilihan kamu? [y/n] ")

if user_yakin == "n":
    exit()

if pilihan_user == oyen_position:
    print(f"Selamat {nama_user} Kamu menang! posisi oyen ada di {oyen_position} dan pilihanmu adalah {pilihan_user}")
else: 
    print(f"Yahh kamu kalah!, posisi oyen ada di {oyen_position}. sedangkan pilihan kamu adalah {pilihan_user}")