import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_nilai.csv')

rata_rata_nilai = df[['nilai_matematika', 'nilai_bahasa_indonesia', 'nilai_ipa', 'nilai_bahasa_inggris']].mean()

rata_rata_nilai.plot(kind='bar', color=['red', 'blue', 'yellow', 'purple'], figsize=(10, 6))
plt.title('Rata-rata Nilai Siswa Berdasarkan Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Rata-rata Nilai')
plt.xticks(rotation=45)
plt.show()

df_lulus = df[df['keterangan'].isin(['Lulus dengan predikat sangat baik', 'Lulus'])]
kelulusan_per_kelas = df_lulus.groupby(['kelas', 'keterangan']).size().reset_index(name='jumlah_siswa')
kelulusan_dipilih = kelulusan_per_kelas[kelulusan_per_kelas['kelas'].isin(['10A', '10B', '10C'])]
labels = kelulusan_dipilih['kelas'] + ', ' + kelulusan_dipilih['keterangan']

plt.figure(figsize=(8, 6))
plt.bar(labels, kelulusan_dipilih['jumlah_siswa'], color='skyblue')
plt.xlabel('Kelas dan Keterangan', fontsize=12)
plt.ylabel('Jumlah Siswa', fontsize=12)
plt.title('Kelulusan Berdasarkan Kelas dan Predikat Baik atau Lebih')
plt.xticks(rotation=15)
plt.show()
