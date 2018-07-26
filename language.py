# user inputs text --> the language text is written in is detected --> text is translated into language of country they are travelling to #

import jinja2
import os
import webapp2

jinja_env = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

from googletrans import Translator

#this handler takes text -from translate.html- and gives it the variable "content" --> translator.translate will translate "content"
class Translation(webapp2.RequestHandler):
    def get(self):
        translator = Translator()
        trans_template = jinja_env.get_template("templates/translate.html")
        html = trans_template.render({
            "content" : self.request.get("content")
        })
        # dest is a variable for the country's abbreviation
        translator.translate(content, dest) #alpha_2 from pycountry

#if original plan to translate doesn't work, just use this
    # translator = Translator(service_urls=[
    #   'translate.google.com'
    #    ])
