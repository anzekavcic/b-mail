from google.appengine.ext import ndb

class Bmail(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    to = ndb.StringProperty()
    subject = ndb.StringProperty()
    msg = ndb.TextProperty()
    from_user = ndb.StringProperty()
    read = ndb.BooleanProperty(default=False)
