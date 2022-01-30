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
                             list(zip(range(1, 7), range(1, 7))))
    def test_set_item_condition(self, search_cond, condition, expected):
        """item_condition is set"""
        # GIVEN an initialized SearchCondition
        # WHEN valid item condition is given
        # THEN item_condition is set
        search_cond.set_item_condition(condition)

        assert search_cond.item_condition == expected

    @pytest.mark.parametrize("invalid_condition",
                             [-1, 0, 7, "hoge", True, None])
    def test_set_invalid_item_condition(self, search_cond, invalid_condition):
        """set_item_condition() raise an exception
        when being passed an invalid item_codition"""
        # GIVEN an initialized SearchCondition
        # WHEN invalid item condition is given
        # THEN set_item_condition() raises an exception

        with pytest.raises(Exception):
            search_cond.set_item_condition(invalid_condition)

    def test_set_deal_status(self, search_cond):
        """deal_status is set"""
        # GIVEN an initialized SearchCondition
        # WHEN valid deal condition is given
        # THEN deal_status is set

        search_cond.set_deal_status(0)

        assert search_cond.deal_status == 0
