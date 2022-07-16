import requests

headers = {
    'accept': 'application/json',
}

params = {
    'region': 'US',
    'lang': 'en',
    'symbols': 'AAPL,BTC-USD,EURUSD=X',
}

response = requests.get('https://yfapi.net/v6/finance/quote', params=params, headers=headers)
