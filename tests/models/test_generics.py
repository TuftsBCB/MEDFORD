import pytest

from medford import MFD
from MEDFORD.models.generics import Entity


@pytest.mark.skip(reason="no such file or directory error")
def test_Keyword_model():
    test_str = "@Keyword key"

    res = MFD._get_unvalidated_blocks(test_str)
    d = MFD._get_dictionizer({}, {})
    dict = d.generate_dict(res)
    a = Entity(**dict)
    assert 1
    print(a)
