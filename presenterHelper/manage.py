from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost/presentDb'


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    manager.run()


'''
http://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask
1. install flsk-migrate
2. run : python manage.py db init
3. add this line : "target_metadata.reflect(engine, only=["user", "sessions","presentations","session_user_link","answers"])" to  env.py in
"def run_migrations_online():" after "engine=..."
4.run : python manage.py db migrate

'''
