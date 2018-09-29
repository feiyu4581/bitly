# coding=utf-8
from __future__ import absolute_import

import os


DEBUG = False
SECRET_KEY = os.urandom(24)

# Database
SQLALCHEMY_DATABASE_URI = 'postgresql://zhuzx@127.0.0.1:5432/bitly'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_RECORD_QUERIES = True
DATABASE_QUERY_TIMEOUT = 0.5
SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 这个参数在flask-sqlalchemy的文档中说将来会去掉，后面可能需要使用flask.teardown_appcontext 自己来完成 自动 commit


try:
    from config.local_settings import *
except ImportError:
    pass
