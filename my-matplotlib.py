import pandas as pd
import matplotlib.pyplot as plt

#buat data dalam bentuk dataframe pandas
data = {
    'Nama' : ['Asep','Budi','Caca', 'Dimas'],
    'Usia' : [17, 30, 40, 17],
    'Nilai Matematika' : [90, 83, 70, 60],
    'Nilai Produktif' : [73, 85, 80, 90],
}
df = pd.DataFrame(data)

# Membuat diagram garis untuk perbandingan nilai matematika dan produktif
plt.figure(figsize=(10, 6)) # Mengatur ukuran grafik(lebar, tinggi)
plt.plot(df['Nama'],df['Nilai Matematika'],label='Nilai Matematika',color='red') # Menambahkan garis untuk nilai matematika
plt.plot(df['Nama'],df['Nilai Produktif'],label='Nilai Produktif',color='blue') # Menambahkan garis untuk nilai produktif
plt.title('Perbandingan Nilai Matematika dan Produktif') # Menambahkan judul
plt.xlabel('Nama') # Menambahkan label pada sumbu x
plt.ylabel('Nilai') # Menambahkan label pada sumbu y
plt.legend() # Menambahkan legenda
plt.show()

# Membuat diagram batang untuk perbandingan nilai matematika dan produktif
# plt.figure(figsize=(10, 6)) # Mengatur ukuran grafik(lebar, tinggi)
# plt.bar(df['Nama'],df['Nilai Matematika'],label='Nilai Matematika') # Menambahkan diagram batang untuk nilai matematika
# plt.bar(df['Nama'],df['Nilai Produktif'],label='Nilai Produktif') # Menambahkan diagram batang untuk nilai produktif
# plt.title('Perbandingan Nilai Matematika dan Produktif') # Menambahkan judul
# plt.xlabel('Mahasiswa') # Menambahkan label pada sumbu x
# plt.ylabel('Nilai') # Menambahkan label pada sumbu y
# plt.legend() # Menambahkan legenda
# plt.show()