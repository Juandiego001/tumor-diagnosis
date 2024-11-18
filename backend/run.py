from core.app import app, HOST, PORT
from core.controllers.ai import bp as bp_ai

app.register_blueprint(bp_ai, url_prefix='/')

if __name__ == '__main__':
  app.run(host=HOST, port=PORT, debug=True)