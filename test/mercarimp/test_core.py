import pytest

from mercarimp.core import SearchCondition


@pytest.fixture()
def search_cond():
    sc = SearchCondition("hoge")
    return sc


class TestSearchCondition:
    def test_init(self, search_cond):
        assert search_cond.keyword == "hoge"


    def test_set_keyword(self, search_cond):
        search_cond.set_keyword("fuga")

        assert search_cond.keyword == "fuga"
