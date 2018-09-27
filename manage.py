# coding=utf-8
from __future__ import absolute_import

from app import create_app
from flask_script import Manager

import os

app = create_app()
manager = Manager(app)


@manager.command
def runserver():
    app.secret_key = os.urandom(24)
    app.run(debug=True)


if __name__ == '__main__':
    manager.run()
