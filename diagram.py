import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_nilai.csv')

nilai_rata_rata_mtk = df['nilai_matematika'].mean()
nilai_rata_rata_indo = df['nilai_bahasa_indonesia'].mean()

nilai_median_mtk = df['nilai_matematika'].median()
nilai_median_indo = df['nilai_bahasa_indonesia'].median()

nilai_modus_mtk = df['nilai_matematika'].mode()[0]
nilai_modus_indo = df['nilai_bahasa_indonesia'].mode()[0]

nilai_std_mtk = df['nilai_matematika'].std()
nilai_std_indo = df['nilai_bahasa_indonesia'].std()

plt.figure(figsize=(10, 6))
plt.bar(['Matematika', 'Bahasa Indonesia'], [nilai_rata_rata_mtk, nilai_rata_rata_indo], color=['blue', 'orange'])
plt.title('Nilai Rata-Rata Matematika dan Bahasa Indonesia')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(['Matematika', 'Bahasa Indonesia'], [nilai_median_mtk, nilai_median_indo], color=['blue', 'orange'])
plt.title('Nilai Median Matematika dan Bahasa Indonesia')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(['Matematika', 'Bahasa Indonesia'], [nilai_modus_mtk, nilai_modus_indo], color=['blue', 'orange'])
plt.title('Nilai Modus Matematika dan Bahasa Indonesia')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(['Matematika', 'Bahasa Indonesia'], [nilai_std_mtk, nilai_std_indo], color=['blue', 'orange'])
plt.title('Standar Matematika dan Bahasa Indonesia')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.show()
