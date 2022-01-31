import pytest
from mercarimp.core_module import CoreModule

@pytest.fixture()
def core_module():
    "instantiate CoreModule"
    c = CoreModule()
    return c


class TestCoreModule:
    def test_init(self, core_module):
        """instantiation succeeds"""

        assert core_module.base_url == "jp.mercari.com"

    def test_query(self, core_module, search_cond_with_attributes):
        """request mercari for html"""
        core_module.query(search_cond_with_attributes)

        assert type(core_module.dom) == bytes
