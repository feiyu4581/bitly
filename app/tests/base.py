# coding=utf-8
from __future__ import absolute_import


from flask import current_app
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = current_app
        self.app.testing = True
        self.client = self.app.test_client()
