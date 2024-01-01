from flask import Flask

application = Flask(__name__)
app = application
app.config['SECRET_KEY'] = 'sentiment_analyser'

from webapp import routes