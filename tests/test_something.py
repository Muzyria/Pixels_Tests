from pages import Page
import pytest
import pages


@pytest.mark.skip
def test_something():
    print("test something")

    assert Page().find_element_by_id('menuDrawer')