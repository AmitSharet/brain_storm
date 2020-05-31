import gzip
from .brain_storm_pb2 import User, Snapshot

UINT_LEN = 4


class Reader:
    """
Class Reader - reads different types of files .mind and .mind.gz filess
Uses protobuf protocol
    """

    def __init__(self, file_path):
        self.reader_formats = ('.mind', '.mind.gz')
        self.file_path = file_path
        self.file = self.open_file()
        self.user = self.read_user()

    def open_file(self):
        if self.file_path.endswith('gz'):
            return gzip.open(self.file_path, 'rb')
        elif self.file_path.endswith('mind'):
            return open(self.file_path, 'rb')
        else:
            raise NotImplementedError(
                f"The objects format is not supported, Try on of these formats : {self.reader_formats}")
            return -1

    def read_user(self):
        user_size = int.from_bytes(self.file.read(UINT_LEN), byteorder='little')
        return self.file.read(user_size)

    def get_user_binary(self):
        return self.user

    @staticmethod
    def read_protobuf_user(binary_user):
        User.FromString(binary_user)

    @staticmethod
    def read_protobuf_snapshot(binary_snapshot):
        Snapshot.FromString(binary_snapshot)

    def __iter__(self):
        return self

    def __next__(self):
        length_of_snapshot = self.file.read(UINT_LEN)
        if length_of_snapshot:
            length_of_snapshot = int.from_bytes(length_of_snapshot, byteorder = 'little')
            return self.file.read(length_of_snapshot)
        else:
            raise StopIteration
