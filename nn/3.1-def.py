# def faktorial(n):
#     if n == 0 :
#         return 1
#     else :
#         return n * faktorial(n -1)

# hasil = faktorial(5)
# print(hasil)

# def bill(angka):
#     if angka %2 == 0:
#         print(f'{angka} adalah bilangan Genap')
#     else:
#         print(f'{angka} adalah bilangan Ganjil')
# bill(3)

# def luasLingkaran(r):
#     phi = 3.14
#     return phi * r**2
# print(luasLingkaran(14))
    
for i in range(10):
    if i % 2 == 0 and i % 3 == 0:
        print(f"{i} Piece Bash")
    elif i % 3 == 0:
        print(f"{i} Piece")
    elif i % 2 == 1:
        print(f"{i} Bash")
    else:
        print(f"{i} Piece")