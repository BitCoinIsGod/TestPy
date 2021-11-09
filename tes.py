import requests

resp = requests.get("https://api.bithumb.com/public/ticker/BTC") 
print(resp.content)
 
