from flask.ext.mail import Message
from threading import Thread
from . import mail
from flask import render_template,current_app

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject, sender='ehsanroman74@gmail.com', recipients=[to])

    # msg.body = render_template(template + '.txt', **kwargs)
    # msg.html = render_template(template + '.html', **kwargs)

    msg.body = 'send mail testing'
    msg.html = '<h3>send mail testing</h3>'

    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr