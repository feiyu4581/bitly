# coding=utf-8
from __future__ import absolute_import

from app.ext import api, db
from app.route import register_route

from flask import Flask



def register_ext(app):
    api.init_app(app)
    api.app = app


def register_model(app):
    from app.link import model

    db.init_app(app)
    db.app = app


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config/__init__.py')

    register_ext(app)
    register_model(app)
    register_route(api)
    
    return app
