from flask.ext.mail import Message
from threading import Thread
from . import mail
from flask import render_template, current_app


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, confirmation_link, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject, sender='interactive.presentation1395@gmail.com', recipients=[to])

    # msg.body = render_template(template + '.txt', **kwargs)
    # msg.html = render_template(template + '.html', **kwargs)

    msg.body = 'click on below link to confirm your account : ' + confirmation_link
    msg.html = '<h3>click on below link to confirm your account :</h3><br><a href="' + confirmation_link + '">+ click this :)</a>'

    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
