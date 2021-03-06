#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "domace")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

class MainHandler_O_meni(BaseHandler):
    def get(self):
        return self.render_template("index-1.html")

class MainHandler_Moji_projekti(BaseHandler):
    def get(self):
        return self.render_template("index-2.html")

class MainHandler_Blog(BaseHandler):
    def get(self):
        return self.render_template("index-3.html")

class MainHandler_Kontakt(BaseHandler):
    def get(self):
        return self.render_template("index-4.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/o-meni', MainHandler_O_meni),
    webapp2.Route('/moji-projekti', MainHandler_Moji_projekti),
    webapp2.Route('/blog', MainHandler_Blog),
    webapp2.Route('/kontakt', MainHandler_Kontakt),
], debug=True)
