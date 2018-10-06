# coding=utf-8
from __future__ import absolute_import

from flask import request, redirect
from flask_restful import Resource

from app.ext import db
from app.utils.link_encode import LinkEncode
from app.link.model import Link

import time


class LinkApi(Resource):
    def post(self):
        long_url = request.json.get('long_url')
        if not long_url:
            return 'Required long url', 400

        expired_time = request.json.get('expired_time', 0)
        if expired_time:
            try:
                expired_time = int(expired_time)
            except ValueError:
                return 'Error Data', 400

            expired_time = int(time.time()) + expired_time

        return {
            'shortlink': Link.generate_new_link(long_url, expired_time),
        }


class ShortLinkApi(Resource):
    def get(self, shortlink=None):
        if not Link.check_shortlink(shortlink):
            return '404 NOT FOUND', 404

        link = Link.get_by_shortlink(shortlink)
        if not link:
            return '404 NOT FOUND', 404

        return redirect(link.url, code=302)
