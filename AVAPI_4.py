#! /usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from alpha_vantage.timeseries import TimeSeries
import matplotlib
import json
import datetime

matplotlib.rcParams['figure.figsize'] = (16, 8)

print('CARREGANDO DADOS...')

# BUSCA A CHAVE DA API ALPHA VANTAGE
ALPHAVANTAGE_API_KEY = 'QKWVUQ6IISGPG3F8'

ts = TimeSeries(key = ALPHAVANTAGE_API_KEY, output_format='pandas')

# BUSCANDO DADOS DE B3SA3...

class Stock:
  def __init__(self, stock_name):
    self.__stock_name = stock_name
    self.__data, self.__metaData = ts.get_daily(symbol = (f'{ stock_name }.SAO'), outputsize = 'compact')
    self.__symbol, self.__SymbolMetaData = ts.get_symbol_search(f'{ stock_name }.SAO')

    self.conn = sqlite3.connect('stock.db')
    self.__data.to_sql(f'{stock_name}', self.conn, if_exists='replace') 
    #self.__symbol.to_sql(f'{self.__symbol}', self.conn, if_exists='replace') 
    print(self.__symbol)
      
  def busca(self, _days):
    date = datetime.datetime.now() - datetime.timedelta(days=_days)
    date_string = date.strftime('%Y-%m-%d')    
    
    #cursos.execute(f'INSERT INTO {self.__stock_name} (date, 1. open, 2. high, 3. low, 4. close, 5. volume) VALUES(?,?,?,?,?)',())    

    query = pd.read_sql(f'SELECT * FROM { self.__stock_name } WHERE date >= "{ date_string }"', self.conn) 
    df = pd.DataFrame(query, columns=['date','4. close'])

    # querySymbol = pd.read_sql(f'SELECT * FROM { self.__stock_name }', self.conn) 
    # dfs = pd.DataFrame(querySymbol, columns=['date','1. symbol', '2. name'])

    print(f'DADOS CARREGADOS DE { self.__stock_name }:')
    print(df)
    #print(dfs)

    return df
    #return dfs

b3sa3_stock = Stock('B3SA3')
petr4_stock = Stock('PETR4')

b3sa3_data = b3sa3_stock.busca(7) # BUSCA POR DADOS DA ÚLTIMA SEMANA
petr4_data = petr4_stock.busca(7) # BUSCA POR DADOS DA ÚLTIMA SEMANA

plt.title('Daily Time Series for the B3SA3 stock (close)')
plt.plot(b3sa3_data['4. close'])
plt.plot(petr4_data['4. close'])

plt.xlabel("YEAR")
plt.ylabel("POINTS")

plt.plot([], label='B3SA3')
plt.legend()

plt.plot([], label='PETR4')
plt.legend()

plt.show()