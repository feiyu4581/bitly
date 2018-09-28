# coding=utf-8
from __future__ import absolute_import

from app import create_app
from flask_script import Manager

import unittest
import os

app = create_app()
manager = Manager(app)


@manager.command
def runserver():
    app.run()


@manager.command
def test():
    from app.tests import test_modules

    for test_module in test_modules:
        suite = unittest.TestLoader().loadTestsFromModule(test_module)
        unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    manager.run()
