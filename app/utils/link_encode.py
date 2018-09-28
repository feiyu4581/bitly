# coding=utf-8
from __future__ import absolute_import

from flask import request

import hashlib
import string
import time


class LinkEncode(object):
    '''
    >>> encode = LinkEncode()
    >>> encode.add('127.0.0.1')
    >>> encode.add(time.time())
    >>> encode.hexdigest()
    '''
    def __init__(self, length=7):
        self.params = []
        self.encode_mapping = string.ascii_letters + string.digits
        self.length = length
        self.base = len(self.encode_mapping)

    def add(self, param):
        self.params.append(str(param))

    def base_encode(self, num):
        digits = []
        while num > 0:
            digits.append(self.encode_mapping[num % self.base])
            num /= self.base

        return ''.join(digits[::-1])

    def hexdigest(self):
        if not self.params:
            raise AttributeError('Need Params')

        digest = int(hashlib.md5(''.join(self.params)).hexdigest(), 16)
        return self.base_encode(digest)[:self.length]

    @staticmethod
    def generate_new_link():
        encode = LinkEncode()
        encode.add(request.remote_addr)
        encode.add(time.time())

        return encode.hexdigest()
