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

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('templates/Main.html')
		self.response.write(template.render())

class UpbeatHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('templates/upbeat.html')
		self.response.write(template.render())


app = webapp2.WSGIApplication([
	('/', MainHandler),('/upbeat',UpbeatHandler)])
