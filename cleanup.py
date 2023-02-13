import pandas as pd
df = pd.read_csv(r'C:\Users\shaanarora\Desktop\export_dataframe.csv')
# print(df)
df.drop(df.columns[0], inplace=True, axis=1)
print(df)
print(type(df['urls']))

for i in range(len(df)):
    # print(df.loc[i, 'urls'])
    if '/url?q' not in df.loc[i, 'urls']:
        df = df.drop(labels=i)

df = df.reset_index()

print(df)

for i in range(len(df)):
    df = df.replace(to_replace=df.loc[i, 'urls'], value=df.loc[i, 'urls'][df.loc[i, 'urls'].find(
        '?q=') + 3:df.loc[i, 'urls'].find('.com') + 5])

df.drop(df.columns[0], inplace=True, axis=1)

print(df)

df.to_csv(r'C:\onlyURLs.csv', header=False, index=False)
