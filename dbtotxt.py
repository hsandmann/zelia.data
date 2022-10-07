import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

db = {
        'eng': 'postgresql+psycopg2',
        'addr': 'localhost',
        'port': '5432',
        'user': 'postgres',
        'pwd': 'Post123321',
        'schema': 'spkio.br.rfb'
    }

strconn = f"{db['eng']}://{db['user']}:{db['pwd']}@{db['addr']}:{db['port']}/{db['schema']}"
engine = create_engine(strconn)

session = Session(engine)


cursor = session.execute(text(
    'SELECT * from cnae'
))
data = []
for (id_cnae, codigo, descricao, id_source) in cursor:
    data.append([id_cnae, codigo, descricao, id_source])

path_train = os.path.join(os.getcwd(), 'train')

for cnae in data:
    path_file = os.path.join(path_train, f'{cnae[0]}.txt')
    out = open(path_file, 'w')
    out.write(cnae[0] + cnae[1] + cnae[2] + cnae[3])
    out.close()
