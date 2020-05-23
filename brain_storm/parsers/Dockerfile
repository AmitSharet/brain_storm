FROM brain_storm-base:latest

ENV MQ rabbitmq://0.0.0.0:5672

CMD python -m brain_storm.parsers run-parser ${PARSER} ${MQ}