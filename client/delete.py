import configparser
from xts.connect import XTSConnect

path = '/Users/entirety/xts/client/config.ini'

cfg = configparser.ConfigParser()
cfg.read(path)

# uid = 'SHAREINDIA_DEL14'
uid = 'IIFL_54900024'

xtsi = XTSConnect(
    apiKey=cfg[uid]['interactive_order_api_key'],
    secretKey=cfg[uid]['interactive_order_secret_key'], 
    root_url=cfg[uid]['root_url'], 
    endpoint=cfg[uid]['interactive_endpoint'],
    login_type='interactive',
    source=cfg[uid]['source'],
    disable_ssl=cfg[uid]['disable_ssl']
)

xtsi.token = None
response = xtsi.interactive_login()
print(response['result']['token'])

xtsm = XTSConnect(
    apiKey=cfg[uid]['market_data_api_key'],
    secretKey=cfg[uid]['market_data_secret_key'], 
    root_url=cfg[uid]['root_url'], 
    endpoint=cfg[uid]['market_endpoint'],
    login_type='market',
    source=cfg[uid]['source'],
    disable_ssl=cfg[uid]['disable_ssl']
)

xtsm.token = None
response = xtsm.marketdata_login()
print(response['result']['token'])

# xt.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOiI1NDkwMDAyNF84M0Q5N0JDRTUzMzc2ODA4ODREMjQxIiwicHVibGljS2V5IjoiODNkOTdiY2U1MzM3NjgwODg0ZDI0MSIsImlhdCI6MTY1NjcyNzY2MSwiZXhwIjoxNjU2ODE0MDYxfQ.c242UgoWIzBio7FvSQXI26K95L5JYSZDdWuFaz3P0pA'

# response = xt.get_order_book()
# if 'result' not in response:
#     print('HAHAHAHAAHHA EXPIRED')
#     xt.token = None
#     response = xt.interactive_login()
#     print(response)
#     print("Interactive Login Access Token: ", xt.token)
#     response = xt.get_order_book()
#     print(response['result'])
    