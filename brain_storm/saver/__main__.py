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
    Saves data from the path to the input field in the database input
    """
    saver = Saver(database)
    with open(path, 'r') as f:
        data = f.read()
        saver.db.save(data, field)


@main.command('run-saver')
@click.argument('database')
@click.argument('mq')
def run_saver(database, mq):
    """
Listens to the message queue and saves the data recieved from there in the database.
     """
    saver = Saver(database)
    if not saver:
        print("Bad input for saver")
        return -1
    mq = furl(mq)
    mq_host, mq_port = str(mq.host), mq.port
    saver.run_savers(mq_host, mq_port)


if __name__ == '__main__':
    main()