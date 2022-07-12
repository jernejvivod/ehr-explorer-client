class ClientException(Exception):
    def __init__(self, status, reason, url):
        self.status = status
        self.reason = reason
        self.url = url
        super().__init__('\'({0}) {1}\' when calling {2}'.format(status, reason, url))
