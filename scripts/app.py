from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
import db

app = Flask(__name__)
app.config['SECRET_KEY'] = '8u3rouhfkjdsfiluh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///views.sqlite'


from routes import *

if __name__ == '__main__':
    app.run(debug=True)
