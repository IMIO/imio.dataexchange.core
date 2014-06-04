# encoding: utf-8

from imio.amqp import BaseConsumer
from imio.amqp import BasePublisher
from imio.amqp import BaseDispatcher
from imio.dataexchange.core.invoice import Invoice
from imio.dataexchange.core.scripts.base import init_dispatcher
from imio.dataexchange.core.scripts.base import init_script


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
    logger_name = 'invoice_dispatcher'
    log_file = 'invoice_dispatcher.log'


def main():
    config = init_script()
    init_dispatcher(config, InvoiceDispatcher, InvoiceConsumer,
                    InvoicePublisher, 'FACT')
