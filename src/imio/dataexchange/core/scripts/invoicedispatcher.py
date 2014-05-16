# encoding: utf-8

from ConfigParser import ConfigParser
from imio.amqp import BaseConsumer
from imio.amqp import BasePublisher
from imio.amqp import BaseDispatcher
from imio.dataexchange.core.invoice import Invoice
import argparse


class InvoiceConsumer(BaseConsumer):
    queue = 'dms.document'
    routing_key = 'FACT'

    def treat_message(self, message):
        self.publisher.publish(message)


class InvoicePublisher(BasePublisher):

    def get_routing_key(self, message):
        return message.routing_key

    def transform_message(self, message):
        return Invoice(message)


class InvoiceDispatcher(BaseDispatcher):
    logger_name = 'document_dispatcher'
    log_file = 'doc_dispatcher.log'


def main():
    parser = argparse.ArgumentParser(description=u"Initialize the database")
    parser.add_argument('config_uri', type=str)

    args = parser.parse_args()
    config = ConfigParser()
    config.read(args.config_uri)

    url = config.get('config', 'rabbitmq.url')
    dispatcher = InvoiceDispatcher(InvoiceConsumer, InvoicePublisher,
                                   '{0}/%2F?connection_attempts=3&'
                                   'heartbeat_interval=3600'.format(url))
    dispatcher.publisher.setup_queue('dms.document.invoice', 'AA')
    dispatcher.publisher.setup_queue('dms.document.invoice', 'BB')
    try:
        dispatcher.start()
    except KeyboardInterrupt:
        dispatcher.stop()
