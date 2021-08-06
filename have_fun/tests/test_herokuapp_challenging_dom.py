import time


def test_herokuapp_challenging_dom(herokuapp_challenging_dom_page):
    assert herokuapp_challenging_dom_page.button.is_displayed(), 'Button not displayed'
    assert herokuapp_challenging_dom_page.success_button.is_displayed(), 'Success Button not displayed'
    assert herokuapp_challenging_dom_page.alert_button.is_displayed(), 'Alert Button not displayed'
    assert herokuapp_challenging_dom_page.get_label_by_name('Definiebas1').is_displayed(), 'Definiebas1 label not displayed'
    herokuapp_challenging_dom_page.get_row_by_index(1).delete.click()
    assert herokuapp_challenging_dom_page.page_url.endswith('delete')
