import webapp2
import jinja2
import os
import pycountry
import language
import requests_toolbelt
import requests
import json
import csv
# from google.appengine.ext import ndb
import requests_toolbelt.adapters.appengine
requests_toolbelt.adapters.appengine.monkeypatch()

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

# class CamAttempt(ndb.Model):
#     link = ndb.StringProperty(required=False)
#
# def Send(cool_link):
#     new_attempt = CamAttempt()
#     new_attempt.link = cool_link
#     new_attempt.put()

class MapHandler(webapp2.RequestHandler):
    def get(self):
        map_template = jinja_env.get_template("templates/map123.html")
        html = map_template.render()
        self.response.write(html)

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
        r_c = requests.get("http://data.fixer.io/api/latest?access_key=f6857a4dc14c06a10a11b4acccd1ddec&base%20=USD")
        json2 = json.loads(r_c.text)
        USD = json2["rates"]["USD"]

        json1 = json.loads(r.text)
        rating = json1["data"]["situation"]["rating"]
        warning = json1["data"]["lang"]["en"]["advice"]
        learn_more = json1["data"]["lang"]["en"]["url_details"]
        #Send(learn_more)
        # new_attempt = CamAttempt.query().get()
        country_3 = c.alpha_3
        currency_get = c.numeric
        country_name = c.name

        try:
            currency = pycountry.currencies.get(numeric = currency_get)
            currency_3 = currency.alpha_3
            currency_name = currency.name
            foreign = json2["rates"][currency_3]
            rate = float(foreign)/float(USD)
        except:
            currency_name = "not in this database"
            rate = "unfortunately"

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
        elif country_ab == "AF":
            lat = 34.55
            long = 68.917
        elif country_ab == "DE":
            lat = 52.503
            long = 12.303
        elif country_ab == "SE":
            lat = 59.32
            long = 17.421
        elif country_ab == "MA":
            lat = 33.969
            long = -6.92
        else:
            lat = 0
            long = 0

        #language = pycountry.languages.get(alpha_2 = country_ab)
        html = country_template.render({
            #"link" : new_attempt.link,
            "name" : country_name,
            "currency" : currency_name,
            "rating" : rating,
            "warning" : warning,
            "learn_more" : learn_more,
            "lat" : lat,
            "long" : long,
            "alpha_2" : language,
            'usd' : USD,
            'rate' : rate,
        })
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/country?(.*)', CountryHandler),
    ('/', MapHandler),
    ('/translate/(.*)', language.Translation)
])
