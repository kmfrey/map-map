import webapp2
import jinja2
import os
import pycountry
import language
import requests_toolbelt
import requests
import json
import csv
import requests_toolbelt.adapters.appengine
requests_toolbelt.adapters.appengine.monkeypatch()

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))



class MapHandler(webapp2.RequestHandler):
    def get(self):
        map_template = jinja_env.get_template("templates/map123.html")
        html = map_template.render()
        self.response.write(html)


r_c = requests.get("http://data.fixer.io/api/latest?access_key=f6857a4dc14c06a10a11b4acccd1ddec&base%20=USD")
json_2 = json.loads(r_c.text)


class CountryHandler(webapp2.RequestHandler):
    def get(self, country_ab):
        country_template = jinja_env.get_template("templates/country.html")
        country_ab = self.request.get("Countries")

        c = pycountry.countries.get(alpha_2 = country_ab)

        language = ""
        with open("countryInfo.txt") as tsv:
            for line in csv.reader(tsv, dialect="excel-tab"):
                if line[0]== country_ab.upper():
                    language = line[15].split(',')[0][:2]


        r = requests.get("https://www.reisewarnung.net/api?country=" + country_ab, verify=False)

        json1 = json.loads(r.text)
        rating = json1["data"]["situation"]["rating"]
        warning = json1["data"]["lang"]["en"]["advice"]
        learn_more = json1["data"]["lang"]["en"]["url_details"]
        country_3 = c.alpha_3
        currency_get = c.numeric
        country_name = c.name
        try:
            currency = pycountry.currencies.get(numeric = currency_get)
            currency_number = currency.alpha_3
            currency_name = currency.name
        except:
            currency_name = "not in this database"

        rating = json1["data"]["situation"]["rating"]
        warning = json1["data"]["lang"]["en"]["advice"]
        learn_more = json1["data"]["lang"]["en"]["url_details"]

        if country_ab == "US":
            lat = 38.89378
            long = -77.15
        elif country_ab == "SG":
            lat = 1.290270
            long = 103.851959
        elif country_ab == "SY":
            lat = 33.510414
            long = 36.278336
        elif country_ab == "CU":
            lat = 23.113592
            long = -82.366592
        elif country_ab == "NG":
            lat = 9.072264
            long = 7.491302
        else:
            lat = 0
            long = 0

        #language = pycountry.languages.get(alpha_2 = country_ab)
        html = country_template.render({
            "name" : country_name,
            "currency" : currency_name,
            "rating" : rating,
            "warning" : warning,
            "learn_more" : learn_more,
            "lat" : lat,
            "long" : long,
            "alpha_2" : language,
        })
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/country?(.*)', CountryHandler),
    ('/', MapHandler),
    ('/translate/(.*)', language.Translation)
])
