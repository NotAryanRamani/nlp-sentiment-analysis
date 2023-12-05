from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sentiment_analyser'

from webapp import routes