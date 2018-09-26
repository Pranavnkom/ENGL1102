from google.appengine.ext import ndb

class Accounts(ndb.Model):
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
