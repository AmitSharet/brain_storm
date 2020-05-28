import pytest

from brain_storm.client import upload_sample

def test_bad_server_url():
    with pytest.raises(ConnectionError):
        bad_server_url='vbdvffsdcd'
        upload_sample(host= bad_server_url, prt = 8000, path = _DATA)


def test_bad_reader_input():
    with pytest.raises(NotImplementedError):
        bad_input_reader='vbdvffsffdcd'
        GeneralDB(bad_input_reader)