from base import BaseHandler
from models import post
from config import PASSWORD

class IndexHandler(RequestHandler):
    def get(self):
        print self.request
        self.render("admin.html")


class LoginHandler(RequestHandler):
    def get(self):
        error_msg = self.get_argument("pass")
        self.render("login.html", error_msg=error_msg)

    def post(self):
        if self.get_argument("pass") == PASSWORD:
            self.set_secure_cookie("status", "Authenticated!")
            self.redirect("/admin")
        else:
            self.redirect("/admin/login?e=1")


class LogoutHandler(RequestHandler):
    def get(self):
        self.clear_all_cookies()
        self.redirect("/")
