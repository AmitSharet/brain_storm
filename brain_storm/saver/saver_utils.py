from ..databases import GeneralDB
import pika
import json


class Saver:
    def __init__(self, database):
        self.db = GeneralDB(database)

    def run_savers(self, mq_host):

        connection = pika.BlockingConnection(pika.ConnectionParameters(mq_host))

        channel = connection.channel()

        channel.exchange_declare(exchange='brain_storm', exchange_type='topic')

        channel.queue_declare('saver')

        channel.queue_bind(
            exchange='brain_storm', queue='saver', routing_key='save.*')

        def callback(ch, method, properties, body):
            field: str = method.routing_key.split('.').pop()
            data = json.loads(body)
            self.db.save(data=data, field=field)

        channel.basic_consume(
            queue='saver', on_message_callback=callback, auto_ack=True)

        print('Saver started listening to queue')

        channel.start_consuming()




