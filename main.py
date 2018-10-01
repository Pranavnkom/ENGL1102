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
        if self.request.get("messages") == "Messages":
            self.redirect("/messages?current_user=" + self.request.get("current_user"))

class IanthePage(webapp2.RequestHandler):
    def get(self):
        ianthe_template = \
                jinja_current_directory.get_template('templates/ianthe.html')
        self.response.write(ianthe_template.render())
    def post(self):
        self.redirect("/home?current_user=" + self.request.get("current_user"))

class RuthvenPage(webapp2.RequestHandler):
    def get(self):
        ruthven_template = \
                jinja_current_directory.get_template('templates/ruthven.html')
        self.response.write(ruthven_template.render())
    def post(self):
        self.redirect("/home?current_user=" + self.request.get("current_user"))

class MaubreyPage(webapp2.RequestHandler):
    def get(self):
        maubrey_template = \
                jinja_current_directory.get_template('templates/maubrey.html')
        self.response.write(maubrey_template.render())
    def post(self):
        self.redirect("/home?current_user=" + self.request.get("current_user"))

class FaubreyPage(webapp2.RequestHandler):
    def get(self):
        faubrey_template = \
                jinja_current_directory.get_template('templates/faubrey.html')
        self.response.write(faubrey_template.render())
    def post(self):
        self.redirect("/home?current_user=" + self.request.get("current_user"))

class MessagesPage(webapp2.RequestHandler):
    def get(self):
        messages_template = \
                jinja_current_directory.get_template('templates/messages.html')
        token = self.request.get("current_user")
        logged = Accounts.query(Accounts.username == token).get()
        current_account = {"logged":logged}
        self.response.write(messages_template.render(current_account))
    def post(self):
        if self.request.get("logout") == "Log Out":
            self.redirect("/")
        if self.request.get("records") == "Go Back to Records":
            self.redirect("/home?current_user=" + self.request.get("current_user"))

class PasswordPage(webapp2.RequestHandler):
    def get(self):
        password_template = \
                jinja_current_directory.get_template('templates/password.html')
        token = self.request.get("current_user")
        logged = Accounts.query(Accounts.username == token).get()
        current_account = {"logged":logged}
        self.response.write(password_template.render(current_account))
    def post(self):
        self.redirect("/messages?current_user=" + self.request.get("current_user"))

class BritishPage(webapp2.RequestHandler):
    def get(self):
        british_template = \
                jinja_current_directory.get_template('templates/british.html')
        self.response.write(british_template.render())
    def post(self):
        self.redirect("/messages?current_user=" + self.request.get("current_user"))

class ELoginPage(webapp2.RequestHandler):
    def get(self):
        elogin_template = \
                jinja_current_directory.get_template('templates/elogin.html')
        self.response.write(elogin_template.render())
    def post(self):
        if self.request.get('but') == "Go Back":
            self.redirect("/home?current_user=" + self.request.get("current_user"))
        else:
            username = "eaubrey" == self.request.get("username")
            password = "polidori" == self.request.get("password")
            if username and password:
                self.redirect("/ehome?current_user=" + self.request.get("current_user"))
            else:
                self.redirect("/eloginerr?current_user=" + self.request.get("current_user"))

class ELoginErrPage(webapp2.RequestHandler):
    def get(self):
        elogin_template = \
                jinja_current_directory.get_template('templates/eloginerr.html')
        self.response.write(elogin_template.render())
    def post(self):
        if self.request.get('but') == "Go Back":
            self.redirect("/home?current_user=" + self.request.get("current_user"))
        else:
            username = "eaubrey" == self.request.get("username")
            password = "polidori" == self.request.get("password")
            if username and password:
                self.redirect("/ehome?current_user=" + self.request.get("current_user"))
            else:
                self.redirect("/eloginerr?current_user=" + self.request.get("current_user"))

class EHomePage(webapp2.RequestHandler):
    def get(self):
        home_template = \
                jinja_current_directory.get_template('templates/ehome.html')
        token = self.request.get("current_user")
        logged = Accounts.query(Accounts.username == token).get()
        current_account = {"logged":logged}
        self.response.write(home_template.render(current_account))

    def post(self):
        self.redirect("/elogin?current_user=" + self.request.get("current_user"))

class UnreadPage(webapp2.RequestHandler):
    def get(self):
        unread_template = \
                jinja_current_directory.get_template('templates/unread.html')
        token = self.request.get("current_user")
        logged = Accounts.query(Accounts.username == token).get()
        current_account = {"logged":logged}
        self.response.write(unread_template.render(current_account))
    def post(self):
        self.redirect("/ehome?current_user=" + self.request.get("current_user"))


app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/loginerror', LoginErrorPage),
    ('/home', HomePage),
    ('/ianthe', IanthePage),
    ('/ruthven', RuthvenPage),
    ('/maubrey', MaubreyPage),
    ('/faubrey', FaubreyPage),
    ('/messages', MessagesPage),
    ('/password', PasswordPage),
    ('/british', BritishPage),
    ('/elogin', ELoginPage),
    ('/eloginerr', ELoginErrPage),
    ('/ehome', EHomePage),
    ('/unread', UnreadPage)
], debug=True)
