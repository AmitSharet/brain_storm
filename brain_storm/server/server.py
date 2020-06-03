from flask import Flask, make_response, request
from ..brain_storm_pb2 import User, Snapshot
from .mq_publsher import _simple_publish
from furl import furl


UINT_32_LEN = 4


def parse_data(binary):
    user_len = int.from_bytes(binary[:UINT_32_LEN], byteorder='little')
    user = User.FromString(binary[UINT_32_LEN:UINT_32_LEN+user_len])
    snapshot = Snapshot.FromString(binary[UINT_32_LEN+user_len:])
    return user, snapshot


supported_queues = {'rabbitmq'}


def run_server(host='localhost', port=8000, publish=_simple_publish, mq_address='rabbitmq://localhost:5672'):
    """Runs the server on the host and port in the input, handles requests from clients and publishes through the
    publisher in the input"""
    server = Flask(__name__)
    mq_url = furl(mq_address)

    if mq_url.scheme not in supported_queues:
        raise Exception(f'message queue not in the right scheme, currently supporting {supported_queues}')
    publisher_host, publisher_port = str(mq_url.host), int(mq_url.port)

    @server.route('/upload', methods=['POST'])
    def upload_snapshot():
        try:
            user, snapshot = parse_data(request.data)
        except Exception as e:
            return make_response(f'Data not in the right format: {e}', 401)
        try:
            publish(user, snapshot, publisher_host, publisher_port)
        except Exception as e:
            print(f'Publisher from the server to the queue failed {e}')
        return make_response('Ok', 200)

    server.run(host=host, port=port, threaded=True)
