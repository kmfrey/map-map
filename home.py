import webapp2
import jinja2
import os
import pycountry
import requests

#request = requests.get("https://www.reisewarnung.net/api", verify=False)

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MapHandler(webapp2.RequestHandler):
    def get(self):
        map_template = jinja_env.get_template("templates/map123.html")
        html = map_template.render()
        self.response.write(html)

class CountryHandler(webapp2.RequestHandler):
    def get(self):
        country_template = jinja_env.get_template("templates/country.html")
        country = "USA"
        english = True
        currency = pycountry.currencies.get(numeric = "840")
        if country == "USA":
            warning = "N/A"
        # else:
        #     request.
        html = country_template.render({
            "name" : country,
            "english" : english,
            "currency" : currency,
        })
        self.response.write(html)

# class FormHandler(webapp2.RequestHandler):
#     def get(self):
#         form_template = jinja_env.get_template("template/orm.html")
#         html = form_template.render()
#         self.response.write(html)

app = webapp2.WSGIApplication([
    ('/USA', CountryHandler),
    ('/', MapHandler),
    #('/form', FormHandler),
])
