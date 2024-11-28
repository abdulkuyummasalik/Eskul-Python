import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_nilai.csv')
pd.DataFrame(df)

ct = df.head(10)

lulus_count = df['keterangan'].value_counts()

# Plotting pie
plt.figure(figsize=(7, 7))
lulus_count.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'])
plt.title('Distribusi Siswa Berdasarkan Keterangan Lulus')
plt.tight_layout()
plt.show()

# Scatter
plt.figure(figsize=(8, 5))
plt.scatter(df['nilai_matematika'], df['nilai_rata_rata'], color='blue')
plt.title("Hubungan Nilai Matematika dan Nilai Rata-rata")
plt.xlabel('Nilai Matematika')
plt.ylabel('Nilai Rata-rata')
plt.tight_layout()
plt.show()
