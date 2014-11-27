# encoding: utf-8


class Request(object):

    def __init__(self, type, parameters, client_id, uid):
        self.type = type
        self.parameters = parameters
        self.client_id = client_id
        self.uid = uid
        self.files = []

    def add_file(self, file):
        self.files.append(file)


class RequestFile(object):

    def __init__(self, uid, metadata):
        self.uid = uid
        self.metadata = metadata
