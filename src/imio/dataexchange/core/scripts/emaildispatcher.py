# -*- coding: utf-8 -*-

from imio.amqp import BaseConsumer
from imio.amqp import BasePublisher
from imio.amqp import BaseDispatcher
from imio.dataexchange.core.dms import Email
from imio.dataexchange.core.scripts.base import init_dispatcher
from imio.dataexchange.core.scripts.base import init_script


class EmailConsumer(BaseConsumer):
    queue = 'dms.email'
    routing_key = 'EMAIL'

    def treat_message(self, message):
        self.publisher.publish(message)


class EmailPublisher(BasePublisher):
    exchange = 'dms.email'

    def get_routing_key(self, message):
        return message.routing_key

    def transform_message(self, message):
        return Email(message)


class EmailDispatcher(BaseDispatcher):
    logger_name = 'email_dispatcher'
    log_file = 'email_dispatcher.log'


def main():
    config = init_script()
    init_dispatcher(
        config,
        EmailDispatcher,
        EmailConsumer,
        EmailPublisher,
        'DELIB',
    )
