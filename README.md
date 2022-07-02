# XTS

### Import libraries
```
import configparser
from xts.connect import XTSConnect
```

### Read credentials from config.ini
```
path = '/Users/entirety/xts/client/config.ini'
cfg = configparser.ConfigParser()
cfg.read(path)
```

### Define the uid: brokername_clientid
#### use the same stored in config.ini
```
uid = 'IIFL_54900004'
```

```
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
print('INTERACTIVE: ',response['result']['token'])
```

```
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
print('MARKET: ',response['result']['token'])
```