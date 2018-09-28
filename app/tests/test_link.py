# coding=utf-8
from __future__ import absolute_import


from .base import BaseTestCase
from app.utils.link_encode import LinkEncode

import time


class TestLinkCase(BaseTestCase):

    def test_encode(self):
        encode = LinkEncode()
        encode.add('127.0.0.1')
        encode.add(time.time())

        print encode.hexdigest()
