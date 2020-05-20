import requests
import click
import json



@click.group()
def main():
    pass


@main.command('get-users')
@click.option('-h', '--host', default= 'localhost', help="BLAH BLAH host")
@click.option('-p', '--port', default= 5000, help="BLAH BLAH port")
def get_users(host,port):
    """
    BLAH BLAH BLAH
    """
    x= requests.get(f'http://{host}:{port}/users')
    print(type(x.content))
    print(x.content)

@main.command('get-user')
@click.option('-h', '--host', default= 'localhost', help="blah host")
@click.option('-p', '--port', default= 5000, help="blah port")
@click.argument('user_id')
def get_user(host,port, user_id):
    """
    BLAH BLAH BLAH
    """
    x = requests.get(f'http://{host}:{port}/users/{user_id}')
    print(x.content)

@main.command('get-snapshots')
@click.option('-h', '--host', default= 'localhost', help="blah host")
@click.option('-p', '--port', default= 5000, help="blah port")
@click.argument('user_id')
def get_snapshots(host,port, user_id):
    """
   BLAH BLAH BLAH
    """
    x = requests.get(f'http://{host}:{port}/users/{user_id}/snapshots')
    print(x.content)


@main.command('get-snapshot')
@click.option('-h', '--host', default= 'localhost', help="hosttt")
@click.option('-p', '--port', default= 5000, help="porttt")
@click.argument('user_id')
@click.argument('snapshot_id')
def get_snapshot(host,port, user_id, snapshot_id):
    """
 BLAH BLAH BLAH
    """
    x= requests.get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}')
    print(x.content)

@main.command('get-result')
@click.option('-h', '--host', default= 'localhost', help="HOST")
@click.option('-p', '--port', default= 5000, help="API PORT")
@click.option('-s', '--save', help="Path to save the result")
@click.argument('user_id')
@click.argument('snapshot_id')
@click.argument('result')
def get_result(host,port, save, user_id, snapshot_id, result):
    """
    BLAH BLAH BLAH
    """
    x = requests.get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}/{result}')
    print(x.content)



if __name__ == '__main__':
    main()
