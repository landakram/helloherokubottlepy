import bottle
import os
from bottle import route, run

app = bottle.default_app()

@route('/')
def hello():
    return 'I\'m running bottle!'

if __name__ == '__main__':
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(os.environ.get('PORT', 5000))
  run(host='0.0.0.0', port=port)
