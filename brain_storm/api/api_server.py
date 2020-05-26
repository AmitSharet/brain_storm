from flask import Flask
from flask import request
import click
import pymongo
from flask_cors import CORS, cross_origin
from bson import json_util
import json
from ..databases import GeneralSaver


def run_api_server(host='127.0.0.1', port=5000, database_url='mongodb://0.0.0.0:27017/'):
    db=GeneralSaver(database_url)

    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @cross_origin()
    @app.route('/users', methods=['GET'])
    def getUsers():
        return db.get_users()


    @cross_origin()
    @app.route('/users/<int:user_id>', methods=['GET'])
    def getUser(user_id):
        return db.get_one_user(user_id)


    @cross_origin()
    @app.route('/users/<int:user_id>/snapshots', methods=['GET'])
    def getUserSnapshots(user_id):
        return db.get_snapshots(user_id)



    @app.route('/users/<int:user_id>/snapshots/<snapshot_id>', methods=['GET'])
    def getUserSnapshot(user_id, snapshot_id):
        return db.get_one_snapshot(user_id, snapshot_id)


    @cross_origin()
    @app.route('/users/<int:user_id>/snapshots/<snapshot_id>/<result_name>', methods=['GET'])
    def getSnapshotResult(user_id, snapshot_id, result_name):
        return db.get_result(user_id,snapshot_id,result_name)



    app.run(host=host, port=port, threaded=True)





