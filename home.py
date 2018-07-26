import webapp2
import jinja2
import os
import german
import pycountry
import language

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))



class MapHandler(webapp2.RequestHandler):
    def get(self):
        map_template = jinja_env.get_template("templates/map123.html")
        html = map_template.render()
        self.response.write(html)

class CountryHandler(webapp2.RequestHandler):
    def get(self,country):
        country_template = jinja_env.get_template("templates/country.html")
        country = ""
### why doesn't name = country workkkkk (ExistingCountries has not attribute alpha_3)

        c = pycountry.countries.get(name = country)
        currency_get = c.numeric
        two = c.alpha_2
        currency = pycountry.currencies.get(numeric = currency_get)
        html = country_template.render({
            "name" : country,
            "currency" : currency,
            "rating" : rating,
            "warning" : warning,
            "learn_more" : learn_more,
        })
        self.response.write(html + country)

# class FormHandler(webapp2.RequestHandler):
#     def get(self):
#         form_template = jinja_env.get_template("template/orm.html")
#         html = form_template.render()
#         self.response.write(html)

app = webapp2.WSGIApplication([
    ('/country/(.*)', CountryHandler),
    ('/', MapHandler),
    ('/translate', language.Translation),
    #('/form', FormHandler),
])
