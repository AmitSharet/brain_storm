client
******


The client is available as brain_storm.client, it helps us upload data about the users and snapshots to the server.

**it exposes the following API:**



>>>    from brain_storm.client import upload_sample
>>> upload_sample(host='127.0.0.1', port=8000, path='sample.mind.gz')
… # upload path to host:port

**And the following CLI:**


      $ python -m cortex.client upload-sample \
      -h/--host '127.0.0.1'             \
      -p/--port 8000                    \
      'snapshot.mind.gz


  toctree::
   :maxdepth: 2
