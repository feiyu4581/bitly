# coding=utf-8
from __future__ import absolute_import

from flask import request
from flask_restful import Resource

from app.ext import db
from app.utils.link_encode import LinkEncode
from app.link.model import Link

import time


class LinkApi(Resource):
    def get(self):
        return {
            'data': 'Hello, Word'
        }

    def post(self):
        long_url = request.json.get('long_url')
        if not long_url:
            return 'Required long url', 400

        return {
            'shortlink': Link.generate_new_link(long_url)
        }
