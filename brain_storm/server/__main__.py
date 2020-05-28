import click
from . import run_server


@click.group()
def main():
    pass


@main.command('run-server')
@click.option('-h', '--host', default='localhost', help="The host of the server")
@click.option('-p', '--port', default=8000, help="The port of the server")
@click.argument('message_queue')
def run(host,port,message_queue):
    """
Starts running the server on the host and port given as input
    """
    try:
        run_server(host = host, port = port, mq_address = message_queue)
    except Exception as e:
        print(f'Got server error: {e}')

if __name__ == '__main__':
    main()