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

    saver = Saver(database)
    with open(path, 'r') as f:
        data = f.read()
        saver.db.save(data, field)


@main.command('run-saver')
@click.argument('database')
@click.argument('mq')
def run_saver(database, mq):

    saver = Saver(database)
    mq = furl(mq)
    mq_host, mq_port = str(mq.host), mq.port
    saver.run_savers(mq_host, mq_port)


if __name__ == '__main__':
    main()