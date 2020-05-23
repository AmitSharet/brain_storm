

class GeneralSaver:
    """General Saver is a layer above all savers which gives ageneral api for any db we want to add
    to our thoughts in the future"""

    def __init__( self, db_url):
        self.db_url = furl(db_url)
        url_scheme=self.db_url.scheme
        if url_scheme in _databases:
            host, port = self.db_url.host , self.db_url.port
            try:
                self.db= _databases[url_scheme](host , port )
            except ConnectionError:
                raiseConnectionError ("DB: Bad db url")

    def get_db_by_name(db_name):  # TODO : Add edge cases
        for file in os.listdir('./brain_storm/saver'):  ##  TODO : fix this
            print(db_name)
            print(file[:-3])
            if file.startswith("_") or not file.endswith(".py"):
                continue  # next loop
            if file[:-4] == db_name and file[-4]=='_':
                module_name = pathlib.Path(file).stem
                print("module name  " + module_name)
                #  TODO :import stuff
                #module = importlib.import_module('.parser_fields.' + module_name, package=__package__)
                print(module)
                ## TODO : return what you imported
                #return (getattr(module, module_name))

        raise NotImplementedError("no parser found with this name")

    def __repr__(self):
        pass

    def save(self, data, field):
        this.db.save()

    def get_users(self):
        pass

    def get_one_user(self, user_id):
        pass

    def get_snapshots(self, user_id):
        pass

    def get_one_snapshot(self, user_id, snapshot_id):
        pass

