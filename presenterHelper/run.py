import os
import logging
from app import create_app, db
from app.models import User
from app import socketio


def main1():
    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))

    with app.app_context():

        db.create_all()

        # create a development user
        if User.query.get(1) is None:

            # parameters : email, password_hash, firstn, lastn, is_audience
            admin = User('admin@yahoo.com', '1234', 'admin', 'adminzade', True)
            admin.is_verified = True;

            try:
                db.session.add(admin)
                db.session.commit()
            except Exception as e:
                print(e)

    socketio.run(app, host="0.0.0.0", port=8000, debug=True)


if __name__ == '__main__':
    main1()

