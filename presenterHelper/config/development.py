import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

file_path =  os.path.join(basedir, '../webapp_user/data')

DEBUG = True
IGNORE_AUTH = True
SECRET_KEY = 'top-secret!'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:farzin@localhost/presentDb'
SQLALCHEMY_TRACK_MODIFICATIONS = True

DATA_DIR = file_path

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True

# these values are hardcoded now , but when deploying time ,
# we shoud get them OS environment variables , especialy for open source projects
# (venv) $ export MAIL_USERNAME=<Gmail username>
# (venv) $ export MAIL_PASSWORD=<Gmail password>
# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD')
MAIL_USERNAME = 'youremail@gmail.com'
MAIL_PASSWORD = 'xxx'
