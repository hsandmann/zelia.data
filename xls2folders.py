import pandas as pd

xlsFile = pd.read_excel('tweets2019.2.xlsx', sheet_name='sheet1')

for index, row in xlsFile.iterrows():
    print(row['classe'], row['texto'])