# encoding: utf-8

from ConfigParser import ConfigParser
from imio.amqp import BaseConsumer
from imio.amqp import BasePublisher
from imio.amqp import BaseDispatcher
from imio.dataexchange.core.invoice import Invoice
from imio.dataexchange.db import DBSession
from imio.dataexchange.db import DeclarativeBase
from imio.dataexchange.db.mappers.file import File
from sqlalchemy import distinct
from sqlalchemy import engine_from_config

import argparse


class InvoiceConsumer(BaseConsumer):
    queue = 'dms.invoice'
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

    init_database(config._sections.get('config'))
    init_amqp(config.get('config', 'rabbitmq.url'))


def init_database(config):
    engine = engine_from_config(config, prefix='sqlalchemy.')
    # Remove the transaction manager
    del DBSession.session_factory.kw['extension']
    DBSession.configure(bind=engine)
    DeclarativeBase.metadata.bind = engine


def init_amqp(amqp_url):
    dispatcher = InvoiceDispatcher(InvoiceConsumer, InvoicePublisher,
                                   '{0}/%2F?connection_attempts=3&'
                                   'heartbeat_interval=3600'.format(amqp_url))

    for client_id in get_client_ids('FACT'):
        dispatcher.publisher.setup_queue('dms.invoice.{0}'.format(client_id),
                                         client_id)
    try:
        dispatcher.start()
    except KeyboardInterrupt:
        dispatcher.stop()


def get_client_ids(file_type):
    query = DBSession.query(distinct(File.client_id))
    query = query.filter(File.type == file_type)
    return [l[0] for l in query.all()]
