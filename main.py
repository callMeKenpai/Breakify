import webapp2
import urllib
import urllib2
import json
import jinja2
import re
import os
import sched, time
import time
from datetime import datetime

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello world")
    def job(self):
        htmlfile = urlib.urlopen("popup.html")
        htmltext = htmlfile.read()
        self.response.write(htmlfile)

class SecondHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello world second page")

app = webapp2.WSGIApplication([('/', MainHandler),('/second', SecondHandler)],
    debug = True)
