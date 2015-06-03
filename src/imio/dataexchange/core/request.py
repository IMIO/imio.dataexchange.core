# encoding: utf-8


class Request(object):

    def __init__(self, type, parameters, application_id, client_id, uid):
        self.type = type
        self.parameters = parameters
        self.application_id = application_id
        self.client_id = client_id
        self.uid = uid
        self.files = []

    def add_file(self, file):
        self.files.append(file)


class RequestFile(object):

    def __init__(self, uid, metadata):
        self.uid = uid
        self.metadata = metadata


class Response(object):

    def __init__(self, uid, **parameters):
        self.uid = uid
        self.parameters = parameters
