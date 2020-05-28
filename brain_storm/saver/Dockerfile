FROM brain_storm-base:latest


CMD cd /usr/src/brain_storm   \
  && python -m brain_storm.saver run-saver mongodb://data_base:27017 rabbitmq://message_queue:5672

#CMD ls