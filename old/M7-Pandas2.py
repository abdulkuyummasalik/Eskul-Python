import pandas as pd

# Dataframe
df1 = pd.DataFrame({
    'Nama' : ['Bintang', 'Syahla', 'Zidan', 'Ujang'],
    'Umur' : [18, 17, 80, None],
    'Gaji' : [5000000, None, 2100000, 3000000]
})
df2 = pd.DataFrame({
    'Nama' : ['Bintang1', 'Syahla1', 'Zidan1', 'Ujang1'],
    'Umur' : [80, 18, 20, None],
    'Gaji' : [5000000, None, 2100000, 3000000]
})

# df_kosong = pd.merge(df1, df2, on='Umur')
# print(df_kosong)

df_kosong = df1['Umur'] = df1['Umur'].fillna(df1['Umur'].mean())

# df_kosong = df_kosong.dropna()
print(df_kosong)



