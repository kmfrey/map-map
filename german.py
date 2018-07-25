import requests
import json
import pycountry

r = requests.get("https://www.reisewarnung.net/api?country=US" # +alpha_2
, verify=False)

json = json.loads(r.text)

print (json["data"]["situation"]["rating"])


dolla = pycountry.currencies.get(name = "US Dollar")
print (dolla)
#change country name into alpha_2 for this, alpha_3 for currency

# r_c = requests.get("http://data.fixer.io/api/latest?access_key=f6857a4dc14c06a10a11b4acccd1ddec&base%20=USD")
# json_2 = json.loads(r_c.text)
#
# print (json_2)
