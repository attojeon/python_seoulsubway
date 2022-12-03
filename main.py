import requests
from urllib.parse import urlencode, quote
import config
import pprint 

bus_infos = []

service_key = config.SERVIDE_KEY
dest_statNm = '고덕'
url = f"http://swopenAPI.seoul.go.kr/api/subway/{service_key}/json/realtimeStationArrival/0/5/{dest_statNm}"
encoded = quote(url)
print(encoded)
# params = {  "KEY": "546647736a61746f38316462455458", 
#             "TYPE": "json", 
#             "SERVICE": "realtimeStationArrival",
#             "statnNm": "고덕"
#          }         
# encoded = urlencode(params).encode()
# print(encoded)
response = requests.get(url, encoded)   
if response.status_code == 200:
    json_obj = response.json()
    pprint.pprint(json_obj)

else:
    print("query error...")


'''
'''
