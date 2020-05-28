import json


def pose(data):
    return json.dumps({'userId': data['user']['userId'], 'datetime': data['snap']['datetime'], 'pose': data['snap']['pose']})