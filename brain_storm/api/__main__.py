import click
from . import run_api_server


@click.group()
def main():
    pass


@main.command('run-server')
@click.option('-h', '--host', default='localhost', help="Host of the api server")
@click.option('-p', '--port', default='5000', help="Port of the api server")
@click.option('-d', '--database', default='mongodb://localhost:27017', help="Database url")
def run_api(host, port, database):
    """
    API server - reflects the information from the database
    """
    try:
        run_api_server(host=host, port=port, database_url=database)
    except Exception as e:
        print(f'Got spi error: {e}')


if __name__ == '__main__':
    main()