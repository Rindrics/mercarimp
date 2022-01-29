import pytest

from mercarimp.core import SearchCondition


@pytest.fixture()
def search_cond():
    """instantiate SearchCondition"""
    sc = SearchCondition("hoge")
    return sc


class TestSearchCondition:
    def test_init(self, search_cond):
        """instantiation succeeds"""
        # GIVEN an initialized SearchCondition
        assert search_cond.keyword == "hoge"


    def test_set_keyword(self, search_cond):
        """keyword can be set"""
        # GIVEN an initialized SearchCondition
        search_cond.set_keyword("fuga")

        assert search_cond.keyword == "fuga"

