# ConsumingAlphaVantageAPI
## Linguagem: Python

Alpha Vantage API
Importação e persistência de preços de ativos
________________________________________________
Eduardo Machado Martins
www.eduardommartins.wordpress.com

ESTRUTURA DO PROJETO

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

1. Conexão com a Alpha Vantage API

•	Para acessar a chave que permite consumir a API da Alpha Vantage, foi realizado o seguinte procedimento:
	
	A chave foi salva num arquivo .txt para não ficar exposta no código 	principal.
	ALPHAVANTAGE_API_KEY = open('alphaVantageKey.txt').read()
	
	A função TimeSeries foi declarada dentro da variável “ts”, com o 	parâmetro output_size no formato “pandas” para que fosse possível 	converter os dados num DataFrame:
	ts = TimeSeries(key = ALPHAVANTAGE_API_KEY, output_format='pandas')


2. Aquisição dos dados utilizando as funções .get_daily e .get_symbol_search.

•	Declaração os atributos da classe para utilização nas funcionalidades da aplicação. A função .get_Daily traz os dados: Date, Open, High, Low, Close e Volume. Já a função .get_symbol_search retorna uma linha com 9 colunas com os dados do ativo como Symbol, Nome, Region, etc. O parãmetro de saída utilizado foi o “Compact”, que retorna os 100 últimos registros. Caso fosse usado “full”, retornaria os registros dos últimos 20 anos.

3. Banco de dados SQLite

•	Declaração da conexão com o nome do banco a ser criado. Após criação, foi utilizada a função .to_sql da biblioteca pandas para criação das tabelas e armazenamento dos dados recebidos. A instrução possui o parâmetro “if_exists” que determina que, caso já existam dados no banco, eles são atualizados, caso não existam, são inseridos de acordo com sua respectiva tabela.


4. Busca dos dados armazenados no SQLite

•	Na função Busca, é solicitado o parâmetro _days, para que se possa calcular quantos dias para trás devem ser trazidos do banco, utilizando a função datetime.timedelta.

•	Nesta seção do código são executadas as intruções responsáveis por selecionar as informações armazenadas no banco de dados, e converte-las para um dataFrame e em seguida printadas no console:


5. Plotagem de gráficos individuais para cada ativo.


6. Plotagem de gráficos individuais para cada ativo.

•	Aqui são executadas as instruções utilizando a biblioteca matplotlib para realizar o plot indvidual dos valores de fechamento dos ativos. É realizada uam verificação para identificar qual o ativo buscado.


7. Instanciando a classe e chamando a função Busca.

•	Instanciando a classe Stock e chamando a função de busca posteriormente, passando o parâmetro _days, que neste caso é 7, referente aos valores da última semana.


8. Resultados

•	Para os últímos 7 dias a aplicação retorna os seguintes resultados:




