import pytest
from pathlib import Path
from brain_storm.client import upload_sample, Reader
_DATA = Path('tests/data/before_parseing.json').absolute()

def test_bad_server_url():
    with pytest.raises(ConnectionError):
        bad_server_url='vbdvffsdcd'
        upload_sample(host= bad_server_url, prt = 8000, path = _DATA)


def test_bad_reader_input():
    with pytest.raises(NotImplementedError):
        bad_input_reader='vbdvffsffdcd'
        Reader(bad_input_reader)