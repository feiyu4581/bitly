# coding=utf-8
from __future__ import absolute_import

from flask import request
from flask_restful import Resource

from app.utils.link_encode import LinkEncode

import time


class LinkApi(Resource):
    def get(self):
        return {
            'data': 'Hello, Word'
        }

    def post(self):

        return {
            'link': LinkEncode.generate_new_link()
        }
