import requests
import json
import xmltodict
import pandas as pd
from df2gspread import df2gspread as d2g

def parser(link):
    # подключение к странице с помощью библиотеки requests
    r = requests.get(link)

    decoded_response = r.content.decode('utf-8')
    response_json = json.loads(
        json.dumps(
            xmltodict.parse(decoded_response)
        )
    )
    
    # отобразить название ключей, чтобы узнать за какие ключи цепляться
    if len(response_json.keys()) == 1:
        for pk in response_json.keys():
            print(pk)
            for ck in response_json[pk]:
                print(ck)
    else:
        print(response_json.keys())
    
    # определяю переменные для нужных мне ключей        
    pk = 'realty-feed'
    ck = 'offer'
    
    # создаю пустой список где будут храниться нужные записи из xml филда
    offers = []
    for offer in response_json[pk][ck]:
        offers.append(offer)

    # создаю dataframe из словаря с помощью pd.json_normalize
    df = pd.json_normalize(offers)
    
parsed_table = parser('xxx')
    
    # далее dataframe можно обработать, например почистить столбци и тд, но перейдем сразу к отправке в гугл таблицы

# отправляю таблицу в google spreadsheets    
def send_to_spreads(df, spreadsheet_key, wks_name):

    d2g.upload(df, spreadsheet_key, wks_name, row_names=True) #загрузка df в google spreadsheets

send_to_spreads(parsed_table, 'xxx', 'test')