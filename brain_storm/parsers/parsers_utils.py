import importlib
import pika
import json
import pathlib
import os


def run_parser_from_mq(mq_host, parser_name, parser):
    connection = pika.BlockingConnection(pika.ConnectionParameters(mq_host))
    channel = connection.channel()
    channel.exchange_declare(exchange='brain_storm', exchange_type='topic')
    channel.queue_declare(parser_name)
    channel.queue_bind(
        exchange='brain_storm', queue=parser_name, routing_key=f'parse.#.{parser_name}.#')

    def callback(ch, method, properties, body):
        message = json.loads(body)
        parsed_result = (parser(message))
        channel.basic_publish(exchange='brain_storm', routing_key=f'save.{parser_name}', body=parsed_result)

    channel.basic_consume( queue=parser_name, on_message_callback=callback, auto_ack=True)
    print(f'{parser_name} is listening to queue now.')
    channel.start_consuming()



def get_parser_by_name(parser_name : str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for file in os.listdir(f'{dir_path}/parser_fields'):
        print(parser_name)
        print(file[:-3])
        if file.startswith("_") or not file.endswith(".py"):
            continue
        if file[:-3] == parser_name:
            module_name = pathlib.Path(file).stem
            module = importlib.import_module('.parser_fields.' + module_name, package=__package__)
            return getattr(module, module_name)

    raise NotImplementedError("no parser found with this name")


def run_parser(field: str, data):
    parser = get_parser_by_name(field)
    return parser(data)


