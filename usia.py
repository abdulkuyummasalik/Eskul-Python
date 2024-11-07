def tentukan_kategori_usia(usia):
    if usia < 0:
        return "Usia tidak valid."
    elif usia <= 2:
        return "Bayi"
    elif usia <= 12:
        return "Anak-anak"
    elif usia <= 17:
        return "Remaja"
    elif usia <= 64:
        return "Dewasa"
    else:
        return "Lansia"

try:
    usia = int(input("Masukkan usia Anda: "))
    kategori = tentukan_kategori_usia(usia)
    print(f"Anda termasuk dalam kategori: {kategori}")
except ValueError:
    print("Harap masukkan angka yang valid untuk usia.")
    
        
    