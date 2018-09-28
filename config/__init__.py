# coding=utf-8
from __future__ import absolute_import

import os


DEBUG = False
SECRET_KEY = os.urandom(24)
SERVER_NAME = 'localhost:8000'

try:
    from config.local_settings import *
except ImportError:
    pass
