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


    @pytest.mark.parametrize("condition, expected",
                             list(zip(range(6), range(6))))
    def test_set_commodity_condition(self, search_cond, condition, expected):
        """commodity_condition is set"""
        # GIVEN an initialized SearchCondition
        # WHEN valid commodity condition is given
        # THEN commodity_condition is set
        search_cond.set_commodity_condition(condition)

        assert search_cond.commodity_condition == expected
