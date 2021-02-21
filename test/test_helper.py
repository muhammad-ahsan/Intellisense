import os
import pytest
from intellisense import helper


@pytest.fixture()
def zip_path() -> str:
    return os.path.dirname(os.path.abspath(__file__)) + '/data/test-vocabulary-en.zip'


@pytest.fixture()
def fake_zip_path() -> str:
    return os.path.dirname(os.path.abspath(__file__)) + '/data/non-existent-vocabulary-en.zip'


def test_existing_vocabulary(zip_path):
    test_vocabulary_set = helper.get_zipped_vocabulary(zip_path)
    assert len(test_vocabulary_set) == 6


def test_non_existing_vocabulary(fake_zip_path):
    with pytest.raises(FileNotFoundError):
        helper.get_zipped_vocabulary(fake_zip_path)


def test_unsupported_vocabulary(zip_path):
    """ French is not supported yet """
    with pytest.raises(ValueError):
        helper.get_vocabulary("fr")
