FROM brain_storm-base:latest

ENV MQ rabbitmq://0.0.0.0:5672

CMD python -m parsers run-parser ${PARSER} ${MQ}