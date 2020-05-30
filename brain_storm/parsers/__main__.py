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
    try:
        with open(data_path, 'r') as file_reader:
            data = file_reader.read()
            parsed_result = run_parser(field, data)
            print(parsed_result)
    except Exception as e:
        print(f'Parser {field} Error : {e}')


@main.command('run-parser')
@click.argument('field')
@click.argument('message_queue_url')
def run_parsers(field, message_queue_url):
    """,
Running parsers in the input and sending results on the message queue
    """
    try:
        mq = furl.furl(message_queue_url)
        mq_host = mq.host
        parser = get_parser_by_name(field)
        run_parser_from_mq(mq_host, field, parser)
    except Exception as e:
        print(f'Parser {field} Error : {e}')


if __name__ == '__main__':
    main()