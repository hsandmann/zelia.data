import requests
import os
import json
import time
import pandas as pd

arquivos = ['tweet2019.1_1.json']

with open('tweets2019.2/tweet2019.2_1.json', 'r') as jsonFileLeitura:
  dadosJson = json.load(jsonFileLeitura)
  df_principal = pd.json_normalize(dadosJson['data'])
  df_tweet = pd.json_normalize(dadosJson['includes']['tweets'])
  df_place = pd.json_normalize(dadosJson['includes']['places'])
  df_user =  pd.json_normalize(dadosJson['includes']['users'])

df_principal.to_excel('tweets_2019.1_chamada_principal.xlsx')
df_tweet.to_excel('tweets_2019.1_tweet.xlsx')
df_place.to_excel('tweets_2019.1_place.xlsx')
df_user.to_excel('tweets_2019.1_user.xlsx')

#df_principal.to_csv('base_exemplo_chamada_principal.csv')
#df_tweet.to_csv('base_exemplo_tweet.csv')
#df_place.to_csv('base_exemplo_place.csv')
#df_user.to_csv('base_exemplo_user.csv')
