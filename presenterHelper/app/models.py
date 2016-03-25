from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class User(db.Model):

    def __init__(self, email, password, firstn, lastn, is_audience):
        self.email = email
        self.set_password(password=password)
        self.firstname = firstn
        self.lastname = lastn

        if (is_audience == True):
            self.is_audience = True
        else:
            self.is_presenter = True

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))

    is_audience = db.Column(db.Boolean(), default=False)
    is_presenter = db.Column(db.Boolean(), default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return '<User %r>' % self.username
