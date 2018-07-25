# user chooses language they want to translate to --> text is translated into language of country they are travelling to #
import jinja2
import os
import webapp2
jinja_env = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

from googletrans import Translator

class Translation(webapp2.RequestHandler):
    def get(self):
        translator = Translator()
        trans_template = jinja_env.get_template("templates/translate.html")
        html = trans_template.render({
            "content" = self.request.get("content")
        })
        translator.translate.(content, dest = #alpha_3 from pycountry)#find a way to import the text users input in translate.html#


#if original plan to translate doesn't work, just use this
    translator = Translator(service_urls=[
      'translate.google.com'
       ])
