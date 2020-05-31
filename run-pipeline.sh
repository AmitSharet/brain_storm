#!/bin/bash

RABBIT='rabbitmq://0.0.0.0:5672'
MONGO='mongodb://0.0.0.0:27017/'

run() {
  echo "Running RabbitMQ docker"
  docker run --rm -d -p 5672:5672 -p 15672:15672 rabbitmq:3-management
  echo "Running MongoDB docker"
  docker run --rm -d -p 27017:27017 mongo:latest
  echo "Wait for RabbitMQ and MongoDB "
  sleep 2m
  python -m brain_storm.server run-server $RABBIT &>/dev/null &
  server=$!
  python -m brain_storm.parsers run-parser 'pose' $RABBIT &>/dev/null &
  pose=$!
  python -m brain_storm.parsers run-parser 'feelings' $RABBIT &>/dev/null &
  feelings=$!
  python -m brain_storm.parsers run-parser 'color_image' $RABBIT &>/dev/null &
  color=$!
  python -m brain_storm.parsers run-parser 'depth_image' $RABBIT &>/dev/null &
  depth=$!
  python -m brain_storm.saver run-saver $MONGO $RABBIT &>/dev/null &
  saver=$!
  python -m brain_storm.api run-server &>/dev/null &
  api=$!


  echo " ctrl+c to stop"
  wait
}

finish() {
  echo ""
  echo "killing brain_storm"
  kill $server $pose $feelings $color $depth $saver $api $gui
  docker container stop $(docker container ls -aq)
}

trap 'finish' SIGINT

run
