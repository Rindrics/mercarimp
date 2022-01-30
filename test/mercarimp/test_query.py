import pytest

from mercarimp.query import construct_query

base_url = "https://jp.mercari.com/search?"


def test_construct_query():
    assert construct_query(base_url, "foo", 1, "sold_out") == (
        base_url
        + "keyword="
        + "foo"
        + "&item_condition_id="
        + str(1)
        + "&status="
        + "sold_out"
    )
