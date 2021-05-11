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

class stock:

    def __init__(self):
        self.b3sa3_data, self.b3sa3_md = ts.get_daily(symbol = ('B3SA3.SAO'), outputsize = 'compact')
        self.b3sa3_symbol = ts.get_symbol_search('B3SA3.SAO')
        
        def buscaB3SA3(self):
                   
            conn = sqlite3.connect('stock.db')
            self.b3sa3_data.to_sql('b3sa3', conn, if_exists='replace')  
            
            self.load_b3sa3 = pd.read_sql('SELECT * FROM b3sa3', conn) 
            
            print('DADOS CARREGADOS DE B3SA3:')
            print(self.load_b3sa3['4. close'])

    # BUSCANDO DADOS DE PETR4
    def  __init__(self):
        self.petr4_data, self.petr4_md = ts.get_daily(symbol = ('PETR4.SAO'), outputsize = 'compact')
        self.petr4_symbol = ts.get_symbol_search('PETR4.SAO')
        
        def buscaPETR4(self):            
            
            conn = sqlite3.connect('stock.db')
            self.petr4_data.to_sql('petr4', conn, if_exists='replace')

            self.load_petr4 = pd.read_sql('SELECT * FROM petr4', conn)  

            print('DADOS CARREGADOS DE PETR4:')
            print(self.load_petr4['4. close'])  

obj = stock()

plt.title('Daily Time Series for the B3SA3 stock (close)')
plt.plot(obj.b3sa3_data['4. close'])
plt.plot(obj.petr4_data['4. close'])

plt.xlabel("YEAR")
plt.ylabel("POINTS")

plt.show()