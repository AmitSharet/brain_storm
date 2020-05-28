FROM brain_storm-base:latest


CMD cd /usr/src/brain_storm   \
  && python -m brain_storm.saver run-saver mongodb://0.0.0.0:27017 rabbitmq://0.0.0.0:5672

#CMD ls