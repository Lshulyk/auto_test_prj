import pytest


@pytest.mark.parametrize('option', ['Option 1', 'Option 2'])
def test_herokuapp(herokuapp_page, option):
    assert herokuapp_page.drop_down_label.is_displayed(), 'Dropdown label not displayed'
    herokuapp_page.drop_down_label.click()
    assert herokuapp_page.drop_down_list_page_title.is_displayed(), 'Dropdown List page not displayed'
    herokuapp_page.drop_down.select_option(option)
    assert herokuapp_page.drop_down.current_option.text == option
