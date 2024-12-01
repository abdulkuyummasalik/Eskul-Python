import pandas as pd

# df = pd.Series([5000, 4000, 3000, 2000, 1000], index=('A', 'B', 'C', 'D', 'E'))
# print(df)

# df = pd.read_csv('data.csv')
# print(df[df['Negara'] == 'Indonesia'])

# dta = {
#     'Negara': ['indonesia', 'singapore', 'japan'],
#     'Ibu_kota': ['jakarta', 'singapore', 'japan'],
#     'Populasi': [200, 300, 400] 
# }

dta = {
    'Nama': ['Asep', 'Bintang', 'Cici', 'Dina'],
    'Umur': [31, 17, 21, 25],
    'Gaji': [5000000, 6200000, 2100000, 3000000] 
}
df = pd.DataFrame(dta)
# df['Gaji'] = [10000000, 41000000, 30000000, 500000]
# df['Nama'] = ['Ayu', 'Usep', 'Sambo', 'Cipew']
df.loc[1, 'Nama'] = "Bibinnn"
print(df)
