from app import db

class light_states(db.Model):
    __tablename__ = "light_states"
    id = db.Column("ID", db.Integer, primary_key=True)
    name = db.Column("name", db.String(20), unique=True, nullable=False)
    state_on = db.Column("state_on", db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"light_states('{self.name}', '{self.state_on}')"
    
    def __init__(self, id, name, state_on):
        self.id = id
        self.name = name
        self.state_on = state_on