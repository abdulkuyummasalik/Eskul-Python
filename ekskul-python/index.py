import pandas as pd
import matplotlib.pyplot as plt

file_path = "siswa_data.csv"
data = pd.read_csv(file_path)
print(f"Data berhasil dimuat dari {file_path}\n")

# Isi nilai kosong
data.fillna(data.mean(numeric_only=True), inplace=True)
print("Nilai kosong telah diisi dengan rata-rata kolom numerik\n")

# Hapus duplikat
data.drop_duplicates(inplace=True)
print("Duplikat data telah dihapus\n")

# Rata-rata
if 'rata_rata_nilai' not in data.columns:
    data['rata_rata_nilai'] = data[['nilai_matematika', 'nilai_bahasa_indonesia', 'nilai_ipa']].mean(axis=1)
    
print("Kolom 'rata_rata_nilai' telah ditambahkan ke dalam data\n")
print(data.isna().sum())


# Histogram
plt.figure(figsize=(10, 6))
plt.hist(data['rata_rata_nilai'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribusi Nilai Rata-Rata Siswa')
plt.xlabel('Rata-Rata Nilai')
plt.ylabel('Frekuensi')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
print("Histogram distribusi nilai rata-rata siswa telah ditampilkan\n")

# Grafik Batang
mean_by_class = data.groupby('kelas')['rata_rata_nilai'].mean()
plt.figure(figsize=(12, 6))
mean_by_class.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Perbandingan Rata-Rata Nilai Antar Kelas')
plt.xlabel('Kelas')
plt.ylabel('Rata-Rata Nilai')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
print("Grafik batang perbandingan rata-rata nilai antar kelas telah ditampilkan\n")


# Ekspor
new_file = "siswa_data_new.csv"
data.to_csv(new_file, index=False)
print(f"Data yang sudah dibersihkan dan dianalisis telah disimpan di {new_file}")
