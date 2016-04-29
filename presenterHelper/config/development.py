import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

file_path = os.path.join(basedir, '../webapp_user/data')
upload_path = os.path.join(basedir, '../webapp_user/data')

DEBUG = True
IGNORE_AUTH = False
SECRET_KEY = 'top-secret!'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:farzin@localhost/presentDb'
SQLALCHEMY_TRACK_MODIFICATIONS = True

DATA_DIR = file_path

ALLOWED_EXTENSIONS = set([ '.png', '.jpg', '.jpeg'])

# after signing in google you should go to below link and allow google to work with less secure apps :
# http://www.google.com/settings/security/lesssecureapps
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'interactive.presentation1395@gmail.com'
MAIL_PASSWORD = 'asdfgh11'
# these values are hardcoded now , but when deploying time ,
# we shoud get them OS environment variables , especialy for open source projects
# (venv) $ export MAIL_USERNAME=<Gmail username>
# (venv) $ export MAIL_PASSWORD=<Gmail password>
# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD')
