import pandas as pd
import random
import os
from os.path import isdir, join


path = join('suicidedb')

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

xlsFile = pd.read_excel('tweets2019.2.xlsx', sheet_name='sheet1')

for index, row in xlsFile.iterrows():

    # remover essa linha quando houver classificacao pelo especialista
    classe = random.choice(['nocivo', 'inofensivo', 'geral'])
    category = random.choice([train, test])
    fpath = join(category, classe)
    if not isdir(fpath):
        os.mkdir(fpath)

    id = row['id']
    texto = str(row['texto'])

    file = open(join(fpath, f'{str(id)}.txt'), 'w')
    file.write(texto)
    file.close()
