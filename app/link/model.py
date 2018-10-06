# coding=utf-8
from __future__ import absolute_import

from sqlalchemy.sql import expression
from app.ext import db
from app.utils.link_encode import LinkEncode

import time


class Link(db.Model):
    shortlink = db.Column(db.String(10), primary_key=True)
    url = db.Column(db.String(256), nullable=False)
    created = db.Column(db.DateTime(), server_default=expression.text('now()'), nullable=False)
    expired_time = db.Column(db.Float(), server_default=expression.text('0'), nullable=False)

    @classmethod
    def create(cls, vals):
        link = cls(**vals)
        db.session.add(link)

        return link

    @classmethod
    def generate_new_link(cls, url, expired_time):
        shortlink = LinkEncode.generate_new_link()

        cls.create({
            'shortlink': shortlink,
            'url': url,
            'expired_time': expired_time
        })

        return shortlink

    @classmethod
    def get_by_shortlink(cls, shortlink):
        link = cls.query.filter_by(shortlink=shortlink).first()
        if link and link.expired_time and time.time() > link.expired_time:
            db.session.delete(link)
            return None

        return link

    @classmethod
    def check_shortlink(cls, shortlink):
        return LinkEncode.check_shortlink(shortlink)
