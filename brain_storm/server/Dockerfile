FROM brain_storm-base:latest

EXPOSE 8000

CMD  cd /usr/src/brain_storm   \
&&ls brain_storm \
&& python -m brain_storm.server run-server -h 127.0.0.1 -p 8000  rabbitmq://0.0.0.0:5672
