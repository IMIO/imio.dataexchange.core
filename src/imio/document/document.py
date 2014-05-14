# encoding: utf-8


def create_document(source):
    """Create a Document instance from a source"""
    kw = {}
    for attr in Document.attrs:
        kw[attr] = getattr(source, attr)
    return Document(**kw)


class Document(object):
    """A GED Document"""
    attrs = ('external_id',
             'version',
             'date',
             'update_date',
             'user',
             'filepath')

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
