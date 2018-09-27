# coding=utf-8
from __future__ import absolute_import

from flask import request
from flask_restful import Resource


class LinkApi(Resource):
    def get(self):
        return {
            'data': 'Hello, Word'
        }

    def post(self):
        long_url = request.json.get('long_url')

        return {
            'link': long_url[:10]
        }
