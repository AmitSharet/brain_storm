server
*******

The server is available as brain_storm.server and
**expose the following API:**

>>> from brain_storm.server import run_server
>>> def print_message(message):
...     print(message)
>>> run_server(host='127.0.0.1', port=8000, publish=print_message)
… # listen on host:port and pass received messages to publish

**And the following CLI:**


$ python -m cortex.server run-server \
      -h/--host '127.0.0.1'          \
      -p/--port 8000                 \
      'rabbitmq://127.0.0.1:5672/'

Note that the API lets callers pass any publishing function, while the CLI only lets them pass a URL to a message queue, to which the server then connects and publishes the data.

The server's job is:
to accept connection, receive the uploaded samples and publish them to its message queue.


  toctree::
   :maxdepth: 2
