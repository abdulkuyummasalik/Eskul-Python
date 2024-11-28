'''
90 - 100 = A
80 - 89 = B
70 - 79 = C
60 - 69 = D
50 - 59 = E
0 - 49 = F

'''
# nilai = int(input("Masukkan nilai Kamu: "))

# if nilai >= 90:
#     grade = 'A'
# elif nilai >= 80:
#     grade = 'B'
# elif nilai >= 70:
#     grade = 'C'
# elif nilai >= 60:
#     grade = 'D'
# elif nilai >= 60:
#     grade = 'E'
# elif nilai >= 50:
#     grade = 'F'
# else:
#     grade = 'E'
    
# print(f'Nilai {nilai} Termasuk{grade}')


# Luas Persegi

# def hitung_luas_persegi(sisi):
#     return sisi ** 2
# sisi = int(input("Masukkan panjang sisi persegi: "))
# luas = hitung_luas_persegi(sisi)
# print(f"Luas persegi dengan sisi {sisi} adalah {luas}.")

    
#    Luas Segitiga
def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi


alas = int(input("Masukkan panjang alas segitiga: "))
tinggi = int(input("Masukkan tinggi segitiga: "))


luas = hitung_luas_segitiga(alas, tinggi)

print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas}.")

    # Ganjil Genap
# for angka in range(1, 101):
#     if angka % 2 == 0:
#         print(f"{angka} = genap")
#     else:
#         print(f"{angka} = ganjil")


    
