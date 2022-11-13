import pandas as pd
import os
from os.path import isdir, join
import random
import subprocess
import tarfile

pathname = 'suicidedbmix'
path = join(pathname)

print(f'removendo: {pathname}')
if isdir(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(path)

os.mkdir(path)
test = join(path, 'test')
os.mkdir(test)
train = join(path, 'train')
os.mkdir(train)

xlsFiles = {
    'tweets_normalizados_2019.xlsx': {'sheetname': '2019_normalizados', 'category': train},
    'tweets_normalizados_2020.xlsx': {'sheetname': '2020_normalizados', 'category': test},
}
mixed = True

labels = ['nocivo', 'protetor', 'geral']
categories = [train, test]

for filename, sn in xlsFiles.items():
    print(f'{filename}/{sn["sheetname"]} to {sn["category"]}')
    xlsFile = pd.read_excel(filename, sheet_name=sn['sheetname'])
    for index, row in xlsFile.iterrows():
        idx_classe = row['classe']
        if idx_classe != idx_classe:
            continue
        
        classe = labels[int(idx_classe) - 1]
        category = random.choice([train, test]) if mixed else sn['category']
        fpath = join(category, classe)
        if not isdir(fpath):
            os.mkdir(fpath)

        id = row['id']
        texto = str(row['texto'])

        file = open(join(fpath, f'{str(id)}.txt'), 'w')
        file.write(texto)
        file.close()

print(f'gerando: {pathname}.tar.gz')
with tarfile.open(f'{pathname}.tar.gz', "w:gz") as tar:
        tar.add(pathname, arcname=os.path.basename(pathname))