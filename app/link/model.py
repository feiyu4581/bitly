# coding=utf-8
from __future__ import absolute_import

from sqlalchemy.sql import expression
from app.ext import db
from app.utils.link_encode import LinkEncode


class Link(db.Model):
    shortlink = db.Column(db.String(10), primary_key=True)
    url = db.Column(db.String(256), nullable=False)
    created = db.Column(db.DateTime(), server_default=expression.text('now()'), nullable=False)

    @classmethod
    def create(cls, vals):
        link = cls(**vals)
        db.session.add(link)

        return link

    @classmethod
    def generate_new_link(cls, url):
        shortlink = LinkEncode.generate_new_link()

        cls.create({
            'shortlink': shortlink,
            'url': url
        })

        return shortlink
