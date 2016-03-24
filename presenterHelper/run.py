__author__ = 'farzin'

import os

from app.models import User
from app import create_app, db


if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))

    with app.app_context():
        db.create_all()

         # create a development user
        if User.query.get(1) is None:
            print('ssssssssssssss')
            admin = User('farzin1', 'ehsanroman74@gmail.com')

            try:
                db.session.add(admin)
                db.session.commit()
            except Exception as e:
                print(e)
    app.run()
