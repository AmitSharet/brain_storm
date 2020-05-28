import requests
import click
import json


@click.group()
def main():
    pass


@main.command('get-users')
@click.option('-h', '--host', default= 'localhost', help="The host to access the API server")
@click.option('-p', '--port', default= 5000, help="The port to access the API server")
def get_users(host, port):
    """
   Gets a users list from the database.
    """
    try:
        users= requests.get(f'http://{host}:{port}/users')
        print(users.content)
    except Exception as e:
        print(f'Command Line Interface error: {e}')


@main.command('get-user')
@click.option('-h', '--host', default= 'localhost', help="The host to access the API server")
@click.option('-p', '--port', default= 5000, help="The port to access the API server")
@click.argument('user_id')
def get_user(host, port, user_id):
    """
    Gets a specific user from the database by it's user-id.
    """
    try:
        user = requests.get(f'http://{host}:{port}/users/{user_id}')
        print(user.content)
    except Exception as e:
        print(f'Command Line Interface error: {e}')


@main.command('get-snapshots')
@click.option('-h', '--host', default= 'localhost', help="The host to access the API server")
@click.option('-p', '--port', default= 5000, help="The port to access the API server")
@click.argument('user_id')
def get_snapshots(host, port, user_id):
    """
   Gets all the snapshots of a specific user from the database by it's user-id.
    """
    try:
        snapshots = requests.get(f'http://{host}:{port}/users/{user_id}/snapshots')
        print(snapshots.content)
    except Exception as e:
        print(f'Command Line Interface error: {e}')


@main.command('get-snapshot')
@click.option('-h', '--host', default= 'localhost', help="The host to access the API server")
@click.option('-p', '--port', default= 5000, help="The port to access the API server")
@click.argument('user_id')
@click.argument('snapshot_id')
def get_snapshot(host, port, user_id, snapshot_id):
    """
Gets one specific snapshot from the database by it's id and the user-id
    """
    try:
        snapshot = requests.get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}')
        print(snapshot.content)
    except Exception as e:
        print(f'Command Line Interface error: {e}')


@main.command('get-result')
@click.option('-h', '--host', default= 'localhost', help="The host to access the API server")
@click.option('-p', '--port', default= 5000, help="The port to access the API server")
@click.option('-s', '--save', help="Path to save the result")
@click.argument('user_id')
@click.argument('snapshot_id')
@click.argument('result')
def get_result(host, port, save, user_id, snapshot_id, result):
    """
    Gets a specific result of a snapshot from the database by it's result name, snapshot-id and user-id.
    """
    try:
        result_data = requests.get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}/{result}')
        if save:
            with open(save, 'w') as file_saver:
                file_saver.write(result_data.content)
        else:
            print(result_data.content)
    except Exception as e:
        print(f'Command Line Interface error: {e}')
        return -1


if __name__ == '__main__':
    main()
