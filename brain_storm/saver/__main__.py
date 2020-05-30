import click
from . import Saver
from furl import furl


@click.group()
def main():
    pass


@main.command('save')
@click.option('-d', '--database', default='mongodb://localhost:27017', help="url of the database ")
@click.argument('field')
@click.argument('path')
def save(field, path, database):
    """
save - Saves data
    """
    try:
        saver = Saver(database)
        with open(path, 'r') as f:
            data = f.read()
            saver.db.save(data, field)
    except Exception as e:
        print(f'Saver Error : {e}')


@main.command('run-saver')
@click.argument('database')
@click.argument('mq')
def run_saver(database, mq):
    """
    Receives urls (+scheme) to a database and a message queue and runs the saver service,
     which listens to the queue and saves message to the database
    """
    try:
        saver = Saver(database)
        mq = furl(mq)
        mq_host = str(mq.host)
        saver.run_savers(mq_host)
    except Exception as e:
        print(f'Saver Error : {e}')


if __name__ == '__main__':
    main()