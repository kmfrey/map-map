from google.appengine.ext import ndb
import pycountry

class Country(ndb.Model):
    def get(self):
        name = "Iran"
        for i in range (0, 250):
            if pycountry.countries.name not == name:
                self.response.write("Country does not exist")
        policies = "sysysy"
        culture = "xxx"
        english = False
        #currency = pycountry.currency.name
