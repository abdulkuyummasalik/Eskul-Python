import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data_siswa.csv')
bin = pd.DataFrame(df)
bin['Tinggi'] = bin['Tinggi'].fillna(bin['Tinggi'].mean())

bin = bin.dropna()
print(bin)