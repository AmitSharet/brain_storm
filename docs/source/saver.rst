Saver
******

The saver is available as brain_storm.saver and

 **expose the following API**:







>>> from brain_storm.saver import Saver
>>> saver = Saver(database_url)
>>> data = …
>>> saver.save('pose', data)





The saver: connects to a database, accepts a topic name and some data, as consumed from the message queue, and saves it to the database.

**It also provides the following CLI:**







$ python -m brain_storm.saver save  -d/--database 'mongodb://0.0.0.0:27017' 'pose'                             \
     'pose.result'





The Saver: accepts a topic name and a path to some raw data, as consumed from the message queue, and saves it to a database.

This way of invocation runs the saver exactly once.




$ python -m cortex.saver run-saver  \
      'postgresql://127.0.0.1:5432' \
      'rabbitmq://127.0.0.1:5672/'



How to add a new Database:
==========================
The saver currently uses mongodb database but supports adding new databases and saving data to them:
To add a new database please follow these steps:

1. Create a file with the name of your database scheme and '_.py' in the end.

2. In the file you created in step 1 add a single class with a name of your choice, in order for things to work the
**class should implement these functions:**

    def __init__(self, host: str, port: int):



    def save(self, data, field): Saves dataof the field


**and for the API to work please implement also:**

    def get_users(self): Gets users list from the database


    def get_one_user(self, user_id): Gets one user from the database by user_id


    def get_snapshots(self, user_id): Gets a list of the snapshots of a user by user_id


    def get_one_snapshot(self, user_id, snapshot_id): Gets one snapshot by user_id and snapshot_id


    def get_result(self, user_id, snapshot_id, result_name): Gets a result of a snapshot from the database by user_id, snapshot_id, result_name.


3. Put the new file you created in brain_storm/databases directory.

  toctree::
   :maxdepth: 2
