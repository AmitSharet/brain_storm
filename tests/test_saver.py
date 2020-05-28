import pytest

from brain_storm.databases import GeneralDB



def test_bad_server_url():
    with pytest.raises(NotImplementedError):
        bad_input_db='vbdvffsffdcd'
        GeneralDB(bad_input_db)