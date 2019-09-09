# encoding: utf-8


class Request(object):
    def __init__(
        self, type, path, parameters, application_id, client_id, uid, cache_duration
    ):
        self.type = type
        self.path = path
        self.parameters = parameters
        self.application_id = application_id
        self.client_id = client_id
        self.uid = uid
        self._cache_duration = cache_duration
        self.files = []
        self.error_count = 0

    def add_file(self, file):
        self.files.append(file)

    @property
    def cache_duration(self):
        if not hasattr(self, '_cache_duration'):
            return 300
        return self._cache_duration


class RequestFile(object):
    def __init__(self, uid, metadata):
        self.uid = uid
        self.metadata = metadata


class Response(object):
    def __init__(self, uid, **parameters):
        self.uid = uid
        self.parameters = parameters
