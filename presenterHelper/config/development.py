import os

basedir = os.path.abspath(os.path.dirname(__file__))
# db_path = os.path.join(basedir, '../data-dev.sqlite')

DEBUG = True
IGNORE_AUTH = True
SECRET_KEY = 'top-secret!'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:farzin@localhost/presentDb'

DATA_DIR = '/home/webapp_user/data'

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
