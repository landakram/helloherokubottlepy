import bottle
import os
from bottle import route, run
from mako.template import Template
from mako.lookup import TemplateLookup

app = bottle.default_app()

@route('/')
def hello():
  lookup = TemplateLookup(
    directories=['templates'], output_encoding='utf-8', encoding_errors='replace')
  template = lookup.get_template('home.mako')
  return template.render()

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  run(host='0.0.0.0', port=port)
