# encoding: utf-8


class Invoice(object):
    """A DMS Invoice"""

    def __init__(self, document):
        self._doc = document
