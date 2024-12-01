import pandas as pd

file_path = 'data.csv'
data = pd.read_csv(file_path)

# 1. Manipulasi string di kolom Gaji (mengubah nilai ke dalam jutaan)
data['Gaji'] = data['Gaji'] // 100000

# 2. Memunculkan ringkasan statistik menggunakan describe()
statistik_ringkasan = data.describe()

# 3. Simpan hasil ke file CSV baru
output_file = '12309481.csv'
data.to_csv(output_file, index=False)

# Menampilkan ringkasan statistik
print("Ringkasan Statistik:")
print(statistik_ringkasan)
