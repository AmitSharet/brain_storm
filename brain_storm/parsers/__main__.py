import click
from . import run_parser_from_mq
from . import get_parser_by_name
from . import run_parser
import furl


@click.group()
def main():
    pass


@main.command('parse')
@click.argument('field')
@click.argument('data_path')
def parse(field: str, data_path: str):
    """
Parsing data from input
    """

    with open(data_path, 'r') as file_reader:
        data = file_reader.read()
        parsed_result = run_parser(field, data)
        print(parsed_result)


@main.command('run-parser')
@click.argument('field')
@click.argument('message_queue_url')
def run_parsers(field, message_queue_url):
    """,
Running parsers in the input and sending results on the message queue
    """

    mq = furl.furl(message_queue_url)
    mq_host, mq_port = mq.host, mq.port
    parser = get_parser_by_name(field)
    run_parser_from_mq(mq_host, mq_port, field, parser)


if __name__ == '__main__':
    main()