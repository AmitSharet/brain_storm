from pymongo import MongoClient, errors
from bson import json_util
import json

class MongoDB:
    """
Database of the mongodb
     """
    name = 'MongoDB'
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        print(self.host)
        print(self.port)
        try:
            self.client = MongoClient(host, int(port), serverSelectionTimeoutMS=120000)
        except errors.ServerSelectionTimeoutError:
            raise ConnectionError

        self.db = self.client["db"]
        self.users = self.db["users"]
        self.snapshots = self.db["snapshots"]

    def insert_user(self, data):
        print(data)
        self.users.update_one({'_id': data['userId']}, {'$set': data}, upsert=True)

    def insert_snap(self, data):
        snapshot_id = data['datetime']
        self.snapshots.update_one({'_id': snapshot_id},
                                  [{'$set': data}], upsert=True)  # create or update

    def save(self, data, field):
        """Saves data in the Mongo DB server"""
        print(field)
        if field == 'user':
            self.insert_user(data)
        else:
            self.insert_snap(data)

        print(f'saving {data}')

    def get_users(self):
        dict_users = {}
        print(list(self.db.users.find(dict_users, {'_id': 0})))
        print(type(list(self.db.users.find(dict_users, {'_id': 0}))))
        return json.dumps(list((self.db.users.find(dict_users, {'_id': 0}))), default=json_util.default)

    def get_one_user(self, user_id):
        user = self.db.users.find_one({'userId': str(user_id)}, {'_id': 0})
        if not user:
            return 'User Not Found', 404
        return json.dumps(user, default=json_util.default), 200 ## TODO : check the 200 works

    def get_snapshots(self, user_id):
        if not self.db.users.find_one({'userId': str(user_id)}):
            return 'User Not Found', 404
        print((list(self.db.snapshots.find({'userId': user_id}, {'_id': 0}))))
        return json.dumps(list(self.db.snapshots.find({'userId': str(user_id)}, {'_id': 0})), default=json_util.default), 200

    def get_one_snapshot(self, user_id, snapshot_id):
        if not self.db.users.find_one({'userId': str(user_id)}):
            return 'User Not Found', 404
        snapshot = self.db.snapshots.find_one({'userId': str(user_id) , 'datetime': snapshot_id })
        print(snapshot)
        if not snapshot:
            return 'Snapshot Not Found For This User', 404
        return json.dumps(snapshot, default=json_util.default), 200

    def get_result(self, user_id, snapshot_id, result_name):
        if not self.db.users.find_one({'userId': str(user_id)}):
            return 'User Not Found', 404
        snapshot = self.db.snapshots.find_one({'userId': str(user_id), 'datetime': snapshot_id})
        if not snapshot:
            return 'Snapshot Not Found For This User', 404
        if result_name not in snapshot:
            return 'Result Is not Available', 404
        return json.dumps(snapshot[result_name], default=json_util.default)  ##TODO: ADD" , 200"



