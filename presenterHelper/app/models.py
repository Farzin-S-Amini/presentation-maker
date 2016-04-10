from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app,url_for
from .exceptions import ValidationError

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))

    is_audience = db.Column(db.Boolean(), default=False)
    is_presenter = db.Column(db.Boolean(), default=False)
    is_verified = db.Column(db.Boolean(), default=False)

    presentations = db.relationship('Presentation', backref='user', lazy='dynamic')

    def __init__(self, email, password, firstn, lastn, is_audience):

        self.email = email
        # self.set_password(password=password)
        self.password_hash = password
        self.firstname = firstn
        self.lastname = lastn

        if is_audience:
            self.is_audience = True
        else:
            self.is_presenter = True

    def set_password(self, password):

        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def send_email_verification(self):
        return None

    def generate_auth_token(self, expires_in=3600):

        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'user_id': self.user_id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['user_id'])

    def generate_confirmation_token(self, expiration=36000):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.user_id}).decode('utf-8')

    @staticmethod
    def verify_register_confirm_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception as e:
            return None
        print(data)
        user = User.query.get(data['confirm'])
        return user

    def __repr__(self):
        return '<User {}>'.format(self.firstname + " " + self.lastname)
class Presentation(db.Model):
    __tablename__ = 'presentations'
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),
                            index=True)
    def get_url(self):
        return url_for('api.get_presentation', id=self.id, _external=True)
    def import_data(self, data):
        try:
            # print(data)
            self.name = data['name']
        except KeyError as e:
            raise ValidationError('Invalid customer: missing ' + e.args[0])
        return self