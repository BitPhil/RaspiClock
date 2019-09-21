from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Develop")

db = SQLAlchemy(app)
#db.create_all();

class light_states(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    state_on = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"light_states('{self.name}', '{self.state_on}')"

from app import views