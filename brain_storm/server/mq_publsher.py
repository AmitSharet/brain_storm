from .proto_to_json import ProtobufToJson
import logging
import os
import pika


def _simple_publish(user, snapshot, mq_host, mq_port):
    """  Publishes to the parsers and saver the user and snapshot data from the input """

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=mq_host))
    channel = connection.channel()
    channel.exchange_declare(exchange='brain_storm', exchange_type='topic')

    current_directory = os.path.abspath('..')
    snapshots_directory_path = f'{current_directory}/Snapshots'
    os.makedirs( snapshots_directory_path, exist_ok=True)
    proto_to_json = ProtobufToJson(snapshots_directory_path)

    body_message, user_message = proto_to_json.user_snap_to_json(user, snapshot)

    routing_key = f'parse.{".".join([field[0].name for field in snapshot.ListFields() if field[0].name != "datetime"])}'
    channel.basic_publish(exchange='brain_storm', routing_key=routing_key, body=body_message)
    channel.basic_publish(exchange='brain_storm', routing_key='save.user', body=user_message)
    connection.close()

