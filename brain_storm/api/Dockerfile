FROM brain_storm-base:latest

CMD cd /usr/src/brain_storm \
    && python -m brain_storm.api run-server -h 0.0.0.0 -p 5000 -d mongodb://0.0.0.0:27017
