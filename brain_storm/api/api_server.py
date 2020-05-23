from flask import Flask
from flask import request
import click
import pymongo
from flask_cors import CORS, cross_origin
from bson import json_util
import json


def run_api_server(host='127.0.0.1', port=5000, database_url='mongodb://0.0.0.0:27017/'):
    client = pymongo.MongoClient(database_url)
    db = client.db

    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @cross_origin()
    @app.route('/users', methods=['GET'])
    def getUsers():
        dict_users = {}
        print(list(db.users.find(dict_users, {'_id': 0})))
        print(type(list(db.users.find(dict_users, {'_id': 0}))))
        return json.dumps(list((db.users.find(dict_users, {'_id': 0}))), default=json_util.default)

    @cross_origin()
    @app.route('/users/<int:user_id>', methods=['GET'])
    def getUser(user_id):
        user = db.users.find_one({'userId': str(user_id)}, {'_id': 0})
        if not user:
            return 'User Not Found', 404
        return json.dumps(user, default=json_util.default), 200 ## TODO : check the 200 works


    @cross_origin()
    @app.route('/users/<int:user_id>/snapshots', methods=['GET'])
    def getUserSnapshots(user_id):
        if not db.users.find_one({'userId': str(user_id)}):
            return 'User Not Found', 404
        print((list(db.snapshots.find({'userId': user_id}, {'_id': 0}))))
        return json.dumps(list(db.snapshots.find({'userId': str(user_id)}, {'_id': 0})), default=json_util.default), 200



    @app.route('/users/<int:user_id>/snapshots/<snapshot_id>', methods=['GET'])
    def getUserSnapshot(user_id, snapshot_id):
        if not db.users.find_one({'userId': str(user_id)}):
            return 'User Not Found', 404
        snapshot = db.snapshots.find_one({'userId': str(user_id) , 'datetime': snapshot_id })
        print(snapshot)
        if not snapshot:
            return 'Snapshot Not Found For This User', 404
        return json.dumps(snapshot, default=json_util.default), 200

    @cross_origin()
    @app.route('/users/<int:user_id>/snapshots/<snapshot_id>/<result_name>', methods=['GET'])
    def getSnapshotResult(user_id, snapshot_id, result_name):
        if not db.users.find_one({'userId': str(user_id)}):
            return 'User Not Found', 404
        snapshot = db.snapshots.find_one({'userId': str(user_id), 'datetime': snapshot_id})
        if not snapshot:
            return 'Snapshot Not Found For This User', 404
        if result_name not in snapshot:
            return 'Result Is not Available', 404
        return json.dumps(snapshot[result_name], default=json_util.default) ,200 ##TODO: CHECK WORKS 200


    app.run(host=host, port=port, threaded=True)





