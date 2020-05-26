from flask import Flask, make_response, request
from .brain_storm_pb2 import User, Snapshot
from .proto_to_json import ProtobufToJson
import logging
import pdb
from google.protobuf.json_format import ParseDict
import os
from furl import furl
import pika
import json
import uuid

UINT_32_LEN_IN_BYTES=4
def parse_data(binary):
    user_len = int.from_bytes(binary[:UINT_32_LEN_IN_BYTES], byteorder='little')
    user = User.FromString(binary[UINT_32_LEN_IN_BYTES:UINT_32_LEN_IN_BYTES+user_len])
    snapshot = Snapshot.FromString(binary[UINT_32_LEN_IN_BYTES+user_len:])
    return user, snapshot


def _simple_publish(user, snapshot, mq_host, mq_port): #TODO : do something with the port in the MQ parameters
    """  Publishesto the parsers and saver the user and snapshot data from the input """

    connection = pika.BlockingConnection(
        pika.ConnectionParameters( host=mq_host ) )
    channel = connection.channel()
    channel.exchange_declare(exchange='brain_storm', exchange_type='topic')

    current_directory = os.path.abspath('..')
    snapshots_directory_path = f'{current_directory}/Snapshots'
    os.makedirs( snapshots_directory_path, exist_ok = True)
    proto_to_json = ProtobufToJson(snapshots_directory_path)

    body_message = proto_to_json.user_snap_to_json(user, snapshot)

    routing_key = f'parse.{".".join([field[0].name for field in snapshot.ListFields() if field[0].name != "datetime"])}'
    logging.warning( "1.1" )#TODO remove logging
    channel.basic_publish( exchange='brain_storm', routing_key=routing_key, body=body_message)
    channel.basic_publish(exchange='brain_storm', routing_key='save.user', body=body_message)
    connection.close()


def run_server(host='localhost', port=8000, publish=_simple_publish, *, mq_address='rabbitmq://localhost:5672'):
    """Runs the server on the host and port in the input, handles requests from clients and publishes through the
    publisher in the input"""
    server = Flask(__name__)
    mq_url = furl( mq_address )

    if mq_url.scheme != 'rabbitmq':
        raise Exception('message queue not in the right scheme, currently supporting rabbit mq') #TODO change
    publisher_host, publisher_port = str(mq_url.host), int(mq_url.port)

    @server.route('/upload', methods=['POST'])
    def upload_snapshot():
        try:
            user, snapshot = parse_data(request.data)
        except:
            return make_response('Data not in the right format', 401) #TODO change
        publish( user,snapshot ,publisher_host, publisher_port )
        return make_response( 'Ok', 200 )

   # if __name__==__main__:
    server.run( host=host, port=port, threaded=True )
