from .reader import Reader
import requests

def upload_sample(path: str, host='127.0.0.1', port=8000):
    """ upload_sample simply reads the sample from the path and uploads to server  """
    file_reader = Reader(path)

    user = file_reader.get_user_binary()
    Reader.read_protobuf_user(user)
    _url = f'http://{host}:{port}/upload'

    UINT_32_LEN = 4
    for binary_snapshot in file_reader:
        Reader.read_protobuf_snapshot(binary_snapshot)

        user_len = int.to_bytes(len(user), UINT_32_LEN, byteorder = 'little')
        message = user_len + user + binary_snapshot

        try:
            requests.post(url=_url, data=message)
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Client couldn't connect to server")


