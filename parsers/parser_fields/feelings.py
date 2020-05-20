import json


def feelings(data):
    return json.dumps({'userId': data['user']['userId'], 'datetime': data['snap']['datetime'], 'feelings': data['snap']['feelings']})
