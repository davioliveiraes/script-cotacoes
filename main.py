import requests
from datetime import datetime

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

requisicao_dict = requisicao.json()
cotacao_dolar = requisicao_dict['USDBRL']['bid']
cotacao_euro = requisicao_dict['EURBRL']['bid']
cotacao_btc = requisicao_dict['BTCBRL']['bid']

print(f"COTAÇÃO ATUALIZADA: {datetime.now()} \n DÓLAR: R${cotacao_dolar} \n EURO: R${cotacao_euro} \n BITCOIN: R${cotacao_btc}")

