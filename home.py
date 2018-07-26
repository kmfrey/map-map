import webapp2
import jinja2
import os
import german
import pycountry

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
        country = "United States"
### why doesn't name = country workkkkk (ExistingCountries has not attribute alpha_3)

        three = pycountry.countries.alpha_3.get(name = country)
        two = pycountry.countries.alpha_2.get(name = country)
        currency = pycountry.currencies.get(alpha_3 = three)
        html = country_template.render({
            "name" : country,
            "currency" : currency,
            "rating" : rating,
            "warning" : warning,
            "learn_more" : learn_more,
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
