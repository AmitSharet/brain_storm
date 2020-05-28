FROM brain_storm-base:latest

#RUN mkdir api
#ADD . /api

EXPOSE 5000

CMD   cd /usr/src/brain_storm   \
 && python -m brain_storm.api run-server -h 0.0.0.0  -d mongodb://0.0.0.0:27017


#WORKDIR /usr/src/brain_storm
#CMD cd /usr/src/brain_storm \
#     && ls /usr/src/brain_storm \
#     && pwd \
#    && python -m brain_storm.api run-server -h 0.0.0.0 -p 5000 -d mongodb://0.0.0.0:27017

