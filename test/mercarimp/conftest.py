import pytest

from mercarimp.search_condition import SearchCondition


@pytest.fixture()
def search_cond():
    """instantiate SearchCondition"""
    sc = SearchCondition("hoge")
    return sc


@pytest.fixture()
def search_cond_with_attributes(search_cond):
    """SearchCondition instance with attributes"""
    search_cond.set_keyword("NIKE")
    search_cond.set_item_condition_id(1)
    search_cond.set_status(0)
    return search_cond
