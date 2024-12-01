import pandas as pd

# dataframe
# data_kosong = {
#     'Nama': ['Asep', 'Bintang', 'Cici', 'Dina', 'Eka'],
#     'Umur': [31, 17, 21, None, 25],
#     'Gaji': [5000000, 6200000, None, 2100000, 3000000]
# }

# df_kosong = pd.DataFrame(data_kosong)
# print(df_kosong)

# df_kosong['umur'] = df_kosong['Umur'].fillna(df_kosong['Umur'].mean())
# print(df_kosong)

# df_kosong = df_kosong.dropna()
# print(df_kosong)

# df_kosong = df_kosong.dropna()
# print(df_kosong)

# df1 = pd.DataFrame({
#     'Nama': ['Asep', 'Bintang', 'Cici', 'Dina', 'Eka'],
#     'Umur': [18, 20, 24, None, 19],
#     'Gaji': [10000, 250000, None, 40000, 50000]
# })

# df2 = pd.DataFrame({
#     'Nama': ['Asep', 'Bintang', 'Cicik', 'Difna', 'Eka'],
#     'Umur': [19, 21, 25, None, 20],
#     'Gaji': [5000000, 6200000, None, 2100000, 3000000]
# })

# df_kosong['umur'] = df_kosong['Umur'].fillna(df_kosong['Umur'].mean())

# print(df_kosong)
# # df_kosong = pd.merge(df1, df2, on='Umur')



df1 = pd.DataFrame({
    'Nama': ['Asep', 'Bintang', 'Cici', 'Dina', 'Eka'],
    'Umur': [18, 20, 24, None, 19],
    'Gaji': [10000, 250000, None, 40000, 50000]
})

df2 = pd.DataFrame({
    'Nama': ['Asep', 'Bintang', 'Cicik', 'Difna', 'Eka'],
    'Umur': [19, 21, 25, None, 20],
    'Gaji': [5000000, 6200000, None, 2100000, 3000000]
})

df_kosong = pd.merge(df1, df2, on='Umur', how='outer', suffixes=('_df1', '_df2'))
df_kosong['Umur'] = df_kosong['Umur'].fillna(df_kosong['Umur'].mean())
print(df_kosong)