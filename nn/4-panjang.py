kata = input('Masukan kata: ')
jumlah_karakter = len(kata)
print(f"Kata '{kata}' memiliki {jumlah_karakter} karakter.")

kata1 = input("Masukan kalimat pertama: ")
kata2 = input("Masukan kalimat kedua: ")
panjang_kata1 = len(kata1)
panjang_kata2 = len(kata2)

if panjang_kata1 > panjang_kata2:
    selisih = panjang_kata1 - panjang_kata2
    print(f"Kalimat pertama '{kata1}' memiliki lebih banyak karakter daripada '{kata2}'. Selisihnya adalah {selisih} karakter.")
elif panjang_kata1 < panjang_kata2:
    selisih = panjang_kata2 - panjang_kata1
    print(f"Kalimat pertama '{kata1}' memiliki lebih sedikit karakter daripada '{kata2}'. Selisihnya adalah {selisih} karakter.")
else:
    print(f"Kalimat '{kata1}' dan '{kata2}' memiliki panjang yang sama, yaitu {panjang_kata1} karakter.")