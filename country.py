from google.appengine.ext import ndb
import pycountry

class Country(ndb.Model):
    def get(self):
        name = ndb.StringProperty(required=True)
        for i in range (0, 250):
        if pycountry.countries.name == name:
            index = pycountry.countries.name[i]
        else:
            self.response.write("Country does not exist")
        policies = ndb.StringProperty(required=True, repeated=True)
        culture = ndb.StringProperty(required=True, repeated=True)
        english = ndb.BooleanProperty(required=True)
        currency = pycountry.currency.name[index]
