import click
from . import run_server


@click.group()
def main():
    pass


@main.command('run-server')
@click.option('-h', '--host', default='localhost', help="TBD")
@click.option('-p', '--port', default=8000, help="TBD")
@click.argument('message_queue')
def run(host,port,message_queue):
    """
   TBD
    """
    run_server(host = host, port = port, mq_address = message_queue)


if __name__ == '__main__':
    main()