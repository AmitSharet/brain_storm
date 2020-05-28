import click
from . import run_api_server


@click.group()
def main():
    pass


@main.command('run-server')
@click.option('-h', '--host', default = 'localhost', help="API HOST")
@click.option('-p', '--port', default = '5000', help="API PORT")
@click.option('-d', '--database', default = 'mongodb://localhost:27017', help="URL SCHEME OF DATABASE DESCRIPTION")
def run_api(host, port, database):
    """
    BLAH BLAH API server
    """
    try:
        run_api_server(host=host, port=port, database_url=database)
    except Exception as e:
        print(f'Got spi error: {e}')

if __name__ == '__main__':
    main()