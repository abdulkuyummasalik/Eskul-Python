import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Nama' : ['Asep','Budi','Caca', 'Dimas'],
    'Usia' : [17, 30, 40, 17],
    'Nilai Matematika' : [90, 83, 70, 60],
    'Nilai Produktif' : [73, 85, 80, 90],
}
df = pd.DataFrame(data)

# Buat diagram bulat sederhana hanya untuk persentase total nilai Matematika dan Produktif
plt.pie([df['Nilai Matematika'].mean(), df['Nilai Produktif'].mean(),df['Usia'].mean()],
        labels=['Nilai Matematika', 'Nilai Produktif', 'Usia'],
        autopct='%1.1f%%', startangle=140)

plt.title('Persentase Rata-rata Nilai Matematika, Produktif dan Usia')
plt.show()
