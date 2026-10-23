# Python 2 (server.dmsmail) shares this namespace with pkg_resources-style packages,
# Python 3 with PEP 420 ones (imio.amqp, imio.dataexchange.db) that pkg_resources ignores
if __import__("sys").version_info[0] == 2:
    __import__("pkg_resources").declare_namespace(__name__)
else:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)
