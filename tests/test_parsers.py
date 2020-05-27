import pytest
import json

from brain_storm.parsers import run_parser
from pathlib import Path




_DATA = Path('tests/data/before_parseing.json').absolute()
_FEELINGS_RESULT = Path('tests/data/after_parsing_feelings.json').absolute()
_POSE_RESULT = Path('tests/data/after_parsing_pose.json').absolute()
#_COLOR_RESULT = Path('tests/data/after_parsing_color.json').absolute()

@pytest.fixture
def data():
    with open(_DATA) as f:
        return json.loads(f.read())

def test_parser_feelings(data):
    result =json.loads((run_parser('feelings',data)))
    with open(_FEELINGS_RESULT) as f:
        assert sorted(result.items())==sorted(json.load(f).items())

def test_parser_pose(data):
    result = json.loads((run_parser('pose', data)))
    with open(_POSE_RESULT) as f:
        assert sorted(result.items()) == sorted(json.load(f).items())

#def test_parser_color(data):
 #   result = json.loads((run_parser('color_image', data)))
  #  with open(_COLOR_RESULT) as f:
   #     assert sorted(result.items()) == sorted(json.load(f).items())


def test_bad_parser_field():
    with pytest.raises(NotImplementedError):
        bad_input_field='vbdvffsdcd'
        bad_input_data='ythgbvfdwqfgt'
        run_parser(bad_input_field,bad_input_data)