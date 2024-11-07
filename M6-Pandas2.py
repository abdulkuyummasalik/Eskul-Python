import pandas as pd

df = pd.read_csv('data.csv')
df = pd.DataFrame(df)

median_gaji = df['Gaji'].median()
max_gaji = df['Gaji'].max()
mode = df['Gaji'].mode()
std = df['Gaji'].std()
min = df['Gaji'].min()

mmedian = df['Umur'].median()
mumur = df['Umur'].max()
mmode = df['Umur'].mode()
mstd = df['Umur'].std()
mmin = df['Umur'].min()
print(f"median{median_gaji}. max {max_gaji}. mode {mode}. std {std}. min {min}. median umur{mmedian}. max umur {mumur}. mode umur {mmode}. std umur {mstd}. min umur {mmin}.")