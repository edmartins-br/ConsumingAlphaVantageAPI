#! /usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from alpha_vantage.timeseries import TimeSeries
import matplotlib
#import json

#CRIANDO A BASE DE DADOS SQLITE3
# database="stock.db"
# conn = sqlite3.connect(database)
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS stocks 
#                 (id INTEGER PRIMARY KEY, 
#                     ticker VARCHAR(10), 
#                     nome VARCHAR(10), 
#                     data DATA, 
#                     ativo VARCHAR(10), 
#                     preco FLOAT)''')

matplotlib.rcParams['figure.figsize'] = (16, 8)

print('CARREGANDO DADOS...')

# BUSCA A CHAVE DA API ALPHA VANTAGE
ALPHAVANTAGE_API_KEY = 'QKWVUQ6IISGPG3F8'

ts = TimeSeries(key = ALPHAVANTAGE_API_KEY, output_format='pandas')

b3sa3_data, b3sa3_md = ts.get_daily(symbol = ('B3SA3.SAO'), outputsize = 'compact')
b3sa3_symbol = ts.get_symbol_search('B3SA3.SAO')
#print('ATIVO: B3SA3', b3sa3_data)

petr4_data, petr4_md = ts.get_daily(symbol = ('PETR4.SAO'), outputsize = 'compact')
petr4_symbol = ts.get_symbol_search('PETR4.SAO')
#print('ATIVO: PETR4', petr4_data)

df_petr4Symbol = pd.DataFrame(petr4_data, columns=['1. symbol', '2. name', '4. region' ])
df_petr4Symbol = df_petr4Symbol.fillna("")

df_b3sa3 = pd.DataFrame(b3sa3_data, columns = ['4. close'])
df_b3sa3 = df_b3sa3.fillna("")

# INSERINDO OS DADOS DA B3SA3 NO BANCO DE DADOS
conn = sqlite3.connect('stock.db')

b3sa3_data.to_sql('b3sa3', conn)  
petr4_data.to_sql('petr4', conn)  


load_b3sa3 = pd.read_sql('SELECT * FROM b3sa3', conn) 
load_petr4 = pd.read_sql('SELECT * FROM petr4', conn)  

print('DADOS CARREGADOS DE B3SA3:')
print(load_b3sa3['4. close'])

print('DADOS CARREGADOS DE PETR4:')
print(load_petr4['4. close'])

print('PETR4 SEARCH SYMBOL RESULT: {} \n'.format(petr4_symbol))

# -----------------------------------------------------------------

# print('B3SA3 DATAFRAME: {}'.format(df_b3sa3))
# df_b3sa3.to_csv (r'b3sa3_dataframe.csv', index = False, header=True)


# print('PETR4 DATAFRAME: ', df_petr4Symbol)    
# df_petr4Symbol.to_csv (r'PETR4_dataframe.csv', index = False, header=True)


#print('B3SA3 SEARCH SYMBOL RESULT: {} \n'.format(b3sa3_symbol))

#PLOTANDOO RESULTADO ADQUIRIDO
plt.title('Daily Time Series for the B3SA3 stock (close)')
plt.plot(b3sa3_data['4. close'])
plt.plot(petr4_data['4. close'])
plt.plot([1, 2, 3], label="test1")
plt.plot([3, 2, 1], label="test2")

plt.xlabel("YEAR")
plt.ylabel("POINTS")

plt.show()

# for index, row in df_b3sa3.iterrows():
#   cursor.execute("INSERT INTO stocks(preco) VALUES (?)", (row['4. close'],))