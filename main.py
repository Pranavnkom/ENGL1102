import webapp2
import jinja2
import os
from models import Accounts

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = \
                jinja_current_directory.get_template('templates/login.html')
        self.response.write(login_template.render())
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        query = Accounts.query(Accounts.username == username, Accounts.password == password).fetch()
        if not query:
            self.redirect("/loginerror")
        else:
            self.redirect("/home?current_user=" + username)

class LoginErrorPage(webapp2.RequestHandler):
    def get(self):
        logine_template = \
                jinja_current_directory.get_template('templates/loginerror.html')
        self.response.write(logine_template.render())
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        query = Accounts.query(Accounts.username == username, Accounts.password == password).fetch()
        if not query:
            self.redirect("/loginerror")
        else:
            self.redirect("/home?current_user=" + username)

class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = \
                jinja_current_directory.get_template('templates/home.html')
        token = self.request.get("current_user")
        logged = Accounts.query(Accounts.username == token).get()
        current_account = {"logged":logged}
        self.response.write(home_template.render(current_account))
    def post(self):
        if self.request.get("logout") == "Log Out":
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/loginerror', LoginErrorPage),
    ('/home', HomePage)
], debug=True)
