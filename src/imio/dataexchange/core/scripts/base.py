# encoding: utf-8

from ConfigParser import ConfigParser
from imio.dataexchange.db import DBSession
from imio.dataexchange.db import DeclarativeBase
from imio.dataexchange.db.mappers.file import File
from sqlalchemy import distinct
from sqlalchemy import engine_from_config

import argparse


def init_script():
    parser = argparse.ArgumentParser(description=u"Initialize the database")
    parser.add_argument('config_uri', type=str)

    args = parser.parse_args()
    config = ConfigParser()
    config.read(args.config_uri)

    init_database(config._sections.get('config'))

    return config


def init_database(config):
    engine = engine_from_config(config, prefix='sqlalchemy.')
    # Remove the transaction manager
    del DBSession.session_factory.kw['extension']
    DBSession.configure(bind=engine)
    DeclarativeBase.metadata.bind = engine


def get_client_ids(file_type):
    query = DBSession.query(distinct(File.client_id))
    query = query.filter(File.type == file_type)
    return [l[0] for l in query.all()]


def init_dispatcher(
    config, dispatcher_cls, consumer_cls, publisher_cls, file_type,
):
    amqp_url = config.get('config', 'rabbitmq.url')
    dispatcher = dispatcher_cls(consumer_cls, publisher_cls,
                                '{0}/%2F?connection_attempts=3&'
                                'heartbeat_interval=3600'.format(amqp_url))

    for client_id in get_client_ids(file_type):
        queue_name = '{0}.{1}'.format(consumer_cls.queue, client_id)
        dispatcher.publisher.setup_queue(queue_name, client_id)
    try:
        dispatcher.start()
    except KeyboardInterrupt:
        dispatcher.stop()
