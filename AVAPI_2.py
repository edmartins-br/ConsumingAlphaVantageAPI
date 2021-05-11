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

# BUSCANDO DADOS DE B3SA3...

b3sa3_data, b3sa3_md = ts.get_daily(symbol = ('B3SA3.SAO'), outputsize = 'compact')
b3sa3_symbol = ts.get_symbol_search('B3SA3.SAO')

# BUSCANDO DADOS DE PETR4
petr4_data, petr4_md = ts.get_daily(symbol = ('PETR4.SAO'), outputsize = 'compact')
petr4_symbol = ts.get_symbol_search('PETR4.SAO')

#CRIANDO A BASE DE DADOS SQLITE3
conn = sqlite3.connect('stock.db')

# INSERINDO O RESAULTADO DA BUSCA, NO BANCO DE DADOS
b3sa3_data.to_sql('b3sa3', conn, if_exists='replace')  
petr4_data.to_sql('petr4', conn, if_exists='replace')  

# CARRREGANDO OS DADOS DO BANCO DE DADOS
load_b3sa3 = pd.read_sql('SELECT * FROM b3sa3', conn) 
load_petr4 = pd.read_sql('SELECT * FROM petr4', conn)  


#  MOSTRA OS DADOS LIDOS NO BANCO
print('DADOS CARREGADOS DE B3SA3:')
print(load_b3sa3['4. close'])

print('DADOS CARREGADOS DE PETR4:')
print(load_petr4['4. close'])

# PLOTANDOO RESULTADO ADQUIRIDO
plt.title('Daily Time Series for the B3SA3 stock (close)')
plt.plot(b3sa3_data['4. close'])
plt.plot(petr4_data['4. close'])

plt.xlabel("YEAR")
plt.ylabel("POINTS")

plt.show()