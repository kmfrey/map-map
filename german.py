import requests
import requests_toolbelt
import json
import pycountry
import requests_toolbelt.adapters.appengine
requests_toolbelt.adapters.appengine.monkeypatch()


r = requests.get("https://www.reisewarnung.net/api?country=US" # +alpha_2
, verify=False)

json1 = json.loads(r.text)

rating = json1["data"]["situation"]["rating"]
warning = json1["data"]["lang"]["en"]["advice"]
learn_more = json1["data"]["lang"]["en"]["url_details"]


dolla = pycountry.currencies.get(name = "US Dollar")
print (dolla)
#change country name into alpha_2 for this, alpha_3 for currency

r_c = requests.get("http://data.fixer.io/api/latest?access_key=f6857a4dc14c06a10a11b4acccd1ddec&base%20=USD")
json_2 = json.loads(r_c.text)
print (json_2)
