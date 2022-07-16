import requests

headers = {'accept': 'application/json', }

params = {'region': 'US',
          'lang': 'en',
          'symbols': 'ETH-USD,BTC-USD,ADA-USD', }

response = requests.get('https://yfapi.net/v6/finance/quote',
                        params=params,
                        headers=headers)
