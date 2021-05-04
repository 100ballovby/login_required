from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(12), unique=True, nullable=True)
    password_hash = db.Column(db.String(128))

    def __str__(self):
        return f'<User {self.username}>'
