import os
from .brain_storm_pb2 import User, Snapshot
from google.protobuf.json_format import MessageToDict
import json
import logging


class ProtobufToJson:
    """A class which makes json of the protobuf input data """
    def __init__(self, save_path):
        self.save_path = save_path

    def _user_to_dict(self, user: User) -> dict:
        return MessageToDict(user)

    def _snap_to_dict(self, snap: Snapshot, user: User) -> dict:
        """Turns the snapshot to a dict, saves the image color and depth data in files and saves the path in the json
        instead, if you want to get to the data afterwards just open the data in the path in read mode."""
        snap_dict = MessageToDict(snap)
        user_data = str(user.user_id) + "-" + user.username
        snap_path = self.save_path + "/" + user_data + "/" + str(snap.datetime) + "/"
        os.makedirs(os.path.dirname(snap_path), exist_ok=True)

        color_path = snap_path + "color.png"
        depth_path = snap_path + "depth.png"
        with open(color_path, 'wb') as save_file:
            save_file.write(snap.color_image.data)
        with open(depth_path, 'w') as save_file:
            i = 0
            for ele in snap.depth_image.data:
                save_file.write(repr(ele) + ',')
                i += 1
            logging.warning('wrote to depth '+str(i))

        # data is transferred from files, not dictionary
        del snap_dict['colorImage']['data']
        del snap_dict['depthImage']['data']
        snap_dict['colorImage']['path'] = color_path
        snap_dict['depthImage']['path'] = depth_path

        return snap_dict


    def user_snap_to_json(self, user: User, snap: Snapshot) -> str:
        """Unites the protobuf user and snapshot to a json"""
        snap_dir_path = '/home/user/Snapshot'  # TODO make this not hard coded
        os.makedirs(os.path.dirname(snap_dir_path), exist_ok=True)
        user_dict, snap_dict = self._user_to_dict(user=user), self._snap_to_dict(snap=snap, user=user)

        return json.dumps({'user': user_dict, 'snap': snap_dict})
