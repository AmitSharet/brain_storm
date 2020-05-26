import os
import pathlib
import inspect
import importlib
from furl import *

databases={}

class GeneralSaver:
    """General Saver is a layer above all savers which gives ageneral api for any db we want to add
    to our thoughts in the future"""

    def __init__( self, db_url):
        pass
        self.db_url = furl(db_url)
        url_scheme=self.db_url.scheme
        db_class = self.get_db_by_name(url_scheme)
        self.db=db_class(self.db_url.host, self.db_url.port)



    def get_db_by_name(self, db_name): #TODO : ADD edge cases
        file_path = os.path.dirname(os.path.realpath(__file__))
        root= pathlib.Path(file_path)
        for file in os.listdir(file_path):
            file =str(file)
            print(db_name)
            print(file[:-4])
            if file.startswith("_") or not file.endswith(".py"):
                continue  # next loop
            if file[:-4] == db_name and file[-4] == '_':
                #scheme=self.db_url.scheme+'_'
                package = f'{root.parent.name}.{root.name}'
                module = importlib.import_module(f'.{pathlib.Path(file).stem}',package=package).__dict__
                for item in module.values():
                    if inspect.isclass(item) and 'save' in item.__dict__:
                        print( item)
                        print(module)
                        return item
        raise NotImplementedError("No parser found with this name")

    def __repr__(self):
        pass

    def save(self, data, field):
        self.db.save(data, field)

    def get_users(self):
        return self.db.get_users()

    def get_one_user(self, user_id):
        return self.db.get_one_user(user_id)

    def get_snapshots(self, user_id):
        return self.db.get_snapshots(user_id)

    def get_one_snapshot(self, user_id, snapshot_id):
        return self.db.get_one_snapshot(user_id, snapshot_id)

    def get_result(self, user_id, snapshot_id, result_name):
        return self.db.get_result(user_id, snapshot_id, result_name)

