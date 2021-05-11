#! /usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from alpha_vantage.timeseries import TimeSeries
import matplotlib
import json

matplotlib.rcParams['figure.figsize'] = (16, 8)

print('CARREGANDO DADOS...')

# BUSCA A CHAVE DA API ALPHA VANTAGE
ALPHAVANTAGE_API_KEY = open('alphaVantageKey.txt').read()

ts = TimeSeries(key = ALPHAVANTAGE_API_KEY, output_format='pandas')
#print(ts.get_symbol_search('B3SA3.SAO', 'PETR4.SAO'))

print('BUSCANDO DADOS DE B3SA3...')
b3sa3_data, b3sa3_md = ts.get_daily(symbol = ('B3SA3.SAO'), outputsize = 'full')
b3sa3_symbol = ts.get_symbol_search('B3SA3.SAO')
print('ATIVO: B3SA3', b3sa3_data)

print('BUSCANDO DADOS DE PETR4...')
petr4_data, petr4_md = ts.get_daily(symbol = ('PETR4.SAO'), outputsize = 'full')
petr4_symbol = ts.get_symbol_search('PETR4.SAO')
print('ATIVO: PETR4', petr4_data)

#CRIANDO A BASE DE DADOS SQLITE3
database="stock.db"
conn = sqlite3.connect(database)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS stocks 
                   (id INTEGER PRIMARY KEY, 
                    ticker VARCHAR(10), 
                    nome VARCHAR(10), 
                    habilitado INT, 
                    data DATA, 
                    ativo VARCHAR(10), 
                    preco INT)''')

print('Recebendo dados da ALPHA VANTAGE...')
df_b3sa3 = pd.DataFrame(b3sa3_data, columns = ['4. close'])
df_b3sa3 = df_b3sa3.fillna("")
print('B3SA3 DATAFRAME: ', df_b3sa3)

df_petr4Symbol = pd.DataFrame(petr4_symbol, columns=['[1. symbol', '2. name', '4. region]'])
df_petr4Symbol = df_petr4Symbol.fillna("")
print('PETR4 DATAFRAME: ', df_petr4Symbol)


print('PETR4 SEARCH SYMBOL RESULT: ', petr4_symbol)
print('B3SA3 SEARCH SYMBOL RESULT: ', b3sa3_symbol)

# PLOTANDOO RESULTADO ADQUIRIDO
# plt.title('Daily Time Series for the B3SA3 stock (close)')
# plt.plot(b3sa3_data['4. close'])
# plt.plot(petr4_data['4. close'])

# plt.xlabel("YEAR")
# plt.ylabel("POINTS")

# plt.show()