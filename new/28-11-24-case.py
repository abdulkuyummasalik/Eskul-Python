import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('28-11-24-data.csv')
sns.barplot(data=df, x="Nama", y="Gaji", hue="Jenis_Kelamin")
plt.title("Rata-rata Gaji Berdasarkan Dapertemen dan Jenis Kelamin")
plt.xlabel("Dapertemen")
plt.ylabel("Rata-rata Gaji")
plt.show()