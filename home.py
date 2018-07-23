import webapp2
import jinja2
import os
import country

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MapHandler(webapp2.RequestHandler):
    def get(self):
        map_template = jinja_env.get_template("templates/map.html")
        html = map_template.render()
        self.response.write(html)

class CountryHandler(webapp2.RequestHandler):
    def get(self):
        country_template = jinja_env.get_template("templates/country.html")
        country = country.Country()
        country.name = self.request.get('name')
        country.policies = self.request.get('policies')
        country.culture = self.request.get('culture')
        if self.request.get('english') == "True":
            country.english = True
        else:
            country.english = False
        country.put()
        html = country_template.render({
            "name" : country.name,
            "policies" : country.policies,
            "culture" : country.culture,
            "english" : country.english,
        })
        self.response.write(html)

# class FormHandler(webapp2.RequestHandler):
#     def get(self):
#         form_template = jinja_env.get_template("template/orm.html")
#         html = form_template.render()
#         self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MapHandler),
    ('/#%s' % country, CountryHandler),
    ('/form', FormHandler),
])
