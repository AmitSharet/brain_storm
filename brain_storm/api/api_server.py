from flask import Flask
from flask_cors import CORS, cross_origin
from ..databases import GeneralDB


def run_api_server(host='127.0.0.1', port=5000, database_url='mongodb://0.0.0.0:27017/'):
    db=GeneralDB(database_url)

    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @cross_origin()
    @app.route('/users', methods=['GET'])
    def get_users():
        return db.get_users()


    @cross_origin()
    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_one_user(user_id):
        return db.get_one_user(user_id)


    @cross_origin()
    @app.route('/users/<int:user_id>/snapshots', methods=['GET'])
    def get_snapshots(user_id):
        return db.get_snapshots(user_id)



    @app.route('/users/<int:user_id>/snapshots/<snapshot_id>', methods=['GET'])
    def get_one_snapshot(user_id, snapshot_id):
        return db.get_one_snapshot(user_id, snapshot_id)


    @cross_origin()
    @app.route('/users/<int:user_id>/snapshots/<snapshot_id>/<result_name>', methods=['GET'])
    def get_result(user_id, snapshot_id, result_name):
        return db.get_result(user_id, snapshot_id, result_name)

    app.run(host=host, port=port, threaded=True)





