from app import db
from models.role import Role

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f"Role('{self.name}')"
role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role.name}')"
