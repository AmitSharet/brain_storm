API
****

The API should be available as brain_storm.api and **expose the following API:**






>>> from cortex.api import run_api_server
>>> run_api_server(
...     host = '127.0.0.1',
...     port = 5000,
...     database_url = 'postgresql://127.0.0.1:5432',
... )
… # listen on host:port and serve data from database_url





**And the following CLI:**







$ python -m cortex.api run-server \
      -h/--host '127.0.0.1'       \
      -p/--port 5000              \
      -d/--database 'postgresql://127.0.0.1:5432'





The API server supports the following RESTful API endpoints :

GET /users
Returns the list of all the supported users, including their IDs and names only.


GET /users/user-id
Returns the specified user's details: ID, name, birthday and gender.

GET /users/user-id/snapshots
Returns the list of the specified user's snapshot IDs and datetimes only.|


GET /users/user-id/snapshots/snapshot-id
Returns the specified snapshot's details: ID, datetime, and the available results' names only (e.g. pose).

Note: Please notice the snapshot id is the timestamp of the snapshot!

GET /users/user-id/snapshots/snapshot-id/result-name

example:
GET /users/user-id/snapshots/snapshot-id/color-image/colorPath

How to add a new Database:
==========================
The saver currently uses mongodb database but supports adding new databases and saving data to them:
To add a new database please follow these steps:

1. Create a file with the name of your database scheme and '_.py' in the end.

2. In the file you created in step 1 add a single class with a name of your choice, in order for things to work the
**class should implement these functions:**

    def __init__(self, host: str, port: int):



    def get_users(self): Gets users list from the database


    def get_one_user(self, user_id): Gets one user from the database by user_id


    def get_snapshots(self, user_id): Gets a list of the snapshots of a user by user_id


    def get_one_snapshot(self, user_id, snapshot_id): Gets one snapshot by user_id and snapshot_id


    def get_result(self, user_id, snapshot_id, result_name): Gets a result of a snapshot from the database by user_id, snapshot_id, result_name.

**And for the saver to work please implement also:**


    def save(self, data, field): Saves dataof the field


3. Put the new file you created in brain_storm/databases directory.

