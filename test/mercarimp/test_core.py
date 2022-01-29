import pytest
from mercarimp.core import SearchCondition


class TestSearchCondition():
    def test_init(self):
        searchCondition = SearchCondition("hoge")

        assert searchCondition.keyword == "hoge"


    def test_set_keyword(self):
        search_condition = SearchCondition("hoge")
        search_condition.set_keyword("fuga")

        assert search_condition.keyword == "fuga"
