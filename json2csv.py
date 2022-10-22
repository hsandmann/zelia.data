import json
from os import listdir
from os.path import isfile, join
from pandas import DataFrame

path = 'tweets2019.2'

jsonFiles = [f for f in listdir(path) if isfile(join(path, f))]
t = 0
ts = {}
for jsonFileName in jsonFiles:
    jsonFile = open(join(path, jsonFileName))

    obj = json.loads(jsonFile.read())
    tweets = obj['data']
    c = 0
    for tweet in tweets:
        id = tweet['id']
        lang = tweet['lang']
        if lang.lower() == 'pt' and id.isnumeric():
            text = tweet['text'].replace('\n', '').replace('"', "'").replace('\t', ' ')
            ts[text] = id
            c = c + 1

    print(f'{jsonFileName}: {c} tweets')

    jsonFile.close()
    t = t + c

df = DataFrame({'id': ts.values(), 'texto': ts.keys()})
df.to_excel(f'{path}.xlsx', sheet_name='sheet1', index=False)

# csvFile = open(f'{path}.csv', 'w')
# for text, id in ts.items():
#     csvFile.write(f'{id},"{text}"\n')
# csvFile.close()

print(f'total: {len(ts)} tweets')
