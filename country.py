from google.appengine.ext import ndb

class Country(ndb.Model):
    name = ndb.StringProperty(required=True)
    policies = ndb.StringProperty(required=True, repeated=True)
    culture = ndb.StringProperty(required=True, repeated=True)
    english = ndb.BooleanProperty(required=True)
