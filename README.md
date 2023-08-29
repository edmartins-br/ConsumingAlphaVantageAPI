# CONSUMINDO A API DA ALPHA VANTAGE
## Linguagem: Python

Alpha Vantage API
Importação e persistência de preços de ativos
________________________________________________
Eduardo Machado Martins

www.eduardommartins.wordpress.com

https://www.linkedin.com/in/eduardommartins/


## ESTRUTURA DO PROJETO

A chave foi adquirida no site da Alpha Vantage.
https://www.alphavantage.co/

Documentação da biblioteca disponiubilizada pela Alpha Vantage
https://www.alphavantage.co/documentation/

Bibliotecas instaladas via linha de comando e impotadas no início do código.

$ pip3 install alpha_vantage

$ pip3 install sqlite3

$ pip3 install pandas

Sistema operacional utilizado: Linux (Ubuntu 20.04 LTS)

Editor de código: VS Code

GitHub: https://github.com/edmartins-br/ConsumingAlphaVantageAPI


## 1. Conexão com a Alpha Vantage API

•	Para acessar a chave que permite consumir a API da Alpha Vantage, foi realizado o seguinte procedimento:
	
	A chave foi salva num arquivo .txt para não ficar exposta no código 	principal.
	ALPHAVANTAGE_API_KEY = open('alphaVantageKey.txt').read()
	
	A função TimeSeries foi declarada dentro da variável “ts”, com o 	parâmetro output_size no formato “pandas” para que fosse possível 	converter os dados num DataFrame:
	ts = TimeSeries(key = ALPHAVANTAGE_API_KEY, output_format='pandas')


## 2. Aquisição dos dados utilizando as funções .get_daily e .get_symbol_search.

•	Declaração os atributos da classe para utilização nas funcionalidades da aplicação. A função .get_Daily traz os dados: Date, Open, High, Low, Close e Volume. Já a função .get_symbol_search retorna uma linha com 9 colunas com os dados do ativo como Symbol, Nome, Region, etc. O parãmetro de saída utilizado foi o “Compact”, que retorna os 100 últimos registros. Caso fosse usado “full”, retornaria os registros dos últimos 20 anos.

## 3. Banco de dados SQLite

•	Declaração da conexão com o nome do banco a ser criado. Após criação, foi utilizada a função .to_sql da biblioteca pandas para criação das tabelas e armazenamento dos dados recebidos. A instrução possui o parâmetro “if_exists” que determina que, caso já existam dados no banco, eles são atualizados, caso não existam, são inseridos de acordo com sua respectiva tabela.


## 4. Busca dos dados armazenados no SQLite

•	Na função Busca, é solicitado o parâmetro _days, para que se possa calcular quantos dias para trás devem ser trazidos do banco, utilizando a função datetime.timedelta.

•	Nesta seção do código são executadas as intruções responsáveis por selecionar as informações armazenadas no banco de dados, e converte-las para um dataFrame e em seguida printadas no console:


## 5. Plotagem de gráficos individuais para cada ativo.

•	Aqui são executadas as instruções utilizando a biblioteca matplotlib para realizar o plot indvidual dos valores de fechamento dos ativos. É realizada uam verificação para identificar qual o ativo buscado.


## 6. Instanciando a classe e chamando a função Busca.

•	Instanciando a classe Stock e chamando a função de busca posteriormente, passando o parâmetro _days, que neste caso é 7, referente aos valores da última semana.

## 7. Resultados

•	Para os últímos 7 dias a aplicação retorna os seguintes resultados:

==================================================

   1. symbol  2. name
   
0  B3SA3.SAO  B3 S.A. - Brasil

==================================================

   date  		   4. close
		  
0  2021-05-05 00:00:00     51.50

1  2021-05-06 00:00:00     50.80

2  2021-05-07 00:00:00     53.34

3  2021-05-10 00:00:00     53.30

4  2021-05-11 00:00:00     52.85

==================================================


==================================================

   1. symbol  2. name
   
0  PETR4.SAO  Petróleo Brasileiro S.A. - Petrobras

==================================================

   date 		   4. close
		  
0  2021-05-05 00:00:00     23.83

1  2021-05-06 00:00:00     23.50

2  2021-05-07 00:00:00     24.38

3  2021-05-10 00:00:00     24.70

4  2021-05-11 00:00:00     25.15

==================================================


Para ver os gráficos, acesse a pasta "Documentos" ou "JupyterNotebook"



