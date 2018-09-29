# coding=utf-8
from __future__ import absolute_import

from app import create_app
from app.ext import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import unittest
import os

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)



@manager.command
def runserver():
    app.run()


@manager.command
def profile():
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app=app.wsgi_app, restrictions=[30])

    runserver()


@manager.command
def test():
    from app.tests import test_modules

    for test_module in test_modules:
        suite = unittest.TestLoader().loadTestsFromModule(test_module)
        unittest.TextTestRunner(verbosity=2).run(suite)


@manager.command
def create_all():
    db.create_all()


@manager.command
def drop_all():
    db.drop_all()


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
