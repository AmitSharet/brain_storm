import click
from . import upload_sample


@click.group()
def main():
    pass

@main.command('upload-sample')
@click.option('-h', '--host', default= 'localhost', help="host of the srver")
@click.option('-p', '--port', default= 8000, help="port of the server")
@click.argument('path')
def upload(host, port, path):
    """
 The client reads the sample from the path, checks if it's written in the
  correct format and uploads it to the server
    """
    try:
        upload_sample(path=path, host=host, port=port)
    except Exception as error:
        print(f'Got client error : {error}')


if __name__ == '__main__':
    main()