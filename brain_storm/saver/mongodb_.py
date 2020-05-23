pass

class MongoDB:
    """
  CLASS DESCRIPTION
     """

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        try:
            self.client = MongoClient(host, int(port), serverSelectionTimeoutMS=120000)
        except errors.ServerSelectionTimeoutError:
            raise ConnectionError

        self.db = self.client["db"]
        self.users = self.db["users"]
        self.snapshots = self.db["snapshots"]

    def insert_user(self, data):
        print(data)
        self.users.update_one({'_id': data['user']['userId']}, {'$set': data['user']}, upsert=True)

    def insert_snap(self, data):
        snapshot_id = data['datetime']
        self.snapshots.update_one({'_id': snapshot_id},
                                  [{'$set': data}], upsert=True)  # create or update

    def save(self, data, field):
        """BLAH BLAH BLAH"""
        print(field)
        if field == 'user':
            self.insert_user(data)
        else:
            self.insert_snap(data)

        print(f'saving {data}')
