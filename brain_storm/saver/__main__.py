import click
from ..databases import GeneralDB
from furl import furl
import pika
import json


@click.group()
def main():
    pass


@main.command('save')
@click.option('-d', '--database', default='mongodb://localhost:27017', help="url of database scheme BLAH BLAH")
@click.argument('field')
@click.argument('result_path')
def save(field, result_path, database):
    """
TBD
    """
    saver = GeneralDB(database)
    with open(result_path, 'r') as f:
        data = f.read()
        saver.save(data, field)


@main.command('run-saver')
@click.argument('database')
@click.argument('mq')
def run_service(database, mq):
    """
    Receives urls (+scheme) to a database and a message queue and runs the saver service, which listens to the queue and saves message to the database
    """
    #database=furl(database)
    #database_host= str(database.host)
    #database_port = int(database.port)
    saver = GeneralDB(database)
    print ("this is mq"+ mq)
    mq = furl(mq)
    mq_host= str(mq.host)
    #mq_port = int(mq.port)
    print("mq- host : "+ mq_host)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(mq_host))

    channel = connection.channel()

    channel.exchange_declare(exchange='brain_storm', exchange_type='topic')

    channel.queue_declare('saver')

    channel.queue_bind(
        exchange='brain_storm', queue='saver', routing_key='save.*')

    def callback(ch, method, properties, body):
        field: str = method.routing_key.split('.').pop()
        data = json.loads(body)
        print(data)
        print(field)
        saver.save( data = data, field=field)

    channel.basic_consume(
    queue='saver', on_message_callback=callback, auto_ack=True)

    print('Saver started listening to queue')

    channel.start_consuming()



if __name__ == '__main__':
    main()