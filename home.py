import webapp2
import jinja2
import os
import pycountry
import language
import requests_toolbelt
import requests
import json
import requests_toolbelt.adapters.appengine
requests_toolbelt.adapters.appengine.monkeypatch()

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))



class MapHandler(webapp2.RequestHandler):
    def get(self):
        map_template = jinja_env.get_template("templates/map123.html")
        html = map_template.render()
        self.response.write(html)


class Constants:
    rating = json1["data"]["situation"]["rating"]
    warning = json1["data"]["lang"]["en"]["advice"]
    learn_more = json1["data"]["lang"]["en"]["url_details"]

r_c = requests.get("http://data.fixer.io/api/latest?access_key=f6857a4dc14c06a10a11b4acccd1ddec&base%20=USD")
json_2 = json.loads(r_c.text)


class CountryHandler(webapp2.RequestHandler):
    def get(self, country):
        country_template = jinja_env.get_template("templates/country.html")
    #    country = ""

        c = pycountry.countries.get(alpha_2 = country)

        r = requests.get("https://www.reisewarnung.net/api?country=" + country
        , verify=False)

        json1 = json.loads(r.text)

        currency_get = c.numeric
        country_name = c.name
        currency = pycountry.currencies.get(numeric = currency_get)
        currency_number = currency.alpha_3
        currency_name = currency.name
        html = country_template.render({
            "name" : country_name,
            "currency" : currency_name,
            "rating" : Constants.rating,
            "warning" : Constants.warning,
            "learn_more" : Constants.learn_more,
        })
        self.response.write(html + country)

###insert into countryhandler



class TestHandler(webapp2.RequestHandler):
    def get(self):
         self.response.write("hello test")

# class FormHandler(webapp2.RequestHandler):
#     def get(self):
#         form_template = jinja_env.get_template("template/orm.html")
#         html = form_template.render()
#         self.response.write(html)

app = webapp2.WSGIApplication([
    ('/country/(.*)', CountryHandler),
    ('/', MapHandler),
    ('/test', TestHandler),
    ('/translate', language.Translation),
    #('/form', FormHandler),
])
