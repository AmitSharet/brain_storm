import click
from . import upload_sample


@click.group()
def main():
    pass

@main.command('upload-sample')
@click.option('-h', '--host', default= 'localhost', help="BLAH BLAH host")
@click.option('-p', '--port', default= 8000, help="BLAH BLAH port")
@click.argument('path')
def upload(host, port, path):
    """
BLAHHHH
    """
    try:
        upload_sample(path=path, host=host, port=port)
    except Exception as error:
        print(f'Got client error : {error}')



if __name__ == '__main__':
    main()