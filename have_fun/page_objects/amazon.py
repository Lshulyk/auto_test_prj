from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from have_fun.page_objects.base_page import BasePage


class CardItem(BasePage):
    def __init__(self, driver, xpath):
        self.driver = driver
        self.xpath = xpath
        self.qty_dd_xpath = f'{self.xpath}//span[contains(@class, "sc-action-quantity")]'
        self.current_qty_xpath = f'{self.qty_dd_xpath}//span[contains(@class, "dropdown-prompt")]'

    @property
    def price(self):
        return self.get_web_element_by_xpath(f'{self.xpath}//span[contains(@class, "sc-price")]')

    @property
    def gift_mark(self):
        el_xpath = f'{self.xpath}//div[contains(@class, "sc-gift-option")]//input'
        self.wait_for_element_enabled(el_xpath)
        return self.get_web_element_by_xpath(el_xpath)

    @property
    def quantity(self):
        return self.get_web_element_by_xpath(f'{self.xpath}//span[contains(@class, "button-dropdown quantity")]')

    def qty_option(self, value):
        qty_menu_xpath = '//div[contains(@class, "a-dropdown") and @aria-hidden="false"]'
        return self.driver.find_element_by_xpath(f'{qty_menu_xpath}[.//a[text()="{value}"]]')

    def select_quantity(self, value):
        self.quantity.click()
        self.qty_option(value).click()
        self.wait_for_element_text(self.current_qty_xpath, value)

    @property
    def current_qty(self):
        return self.driver.find_element_by_xpath(self.current_qty_xpath)


class AmazonPage(BasePage):

    @property
    def search_input(self):
        xpath = '//div[contains(@class, "search-field")]//input'
        return self.driver.find_element_by_xpath(xpath)

    @property
    def search_button(self):
        return self.get_web_element_by_xpath('//input[contains(@id, "search-submit-button")]')

    @property
    def search_dropdown(self):
        return self.driver.find_element_by_xpath('//div[contains(@id, "search-dropdown")]')

    @property
    def search_dd_menu(self):
        return self.driver.find_element_by_xpath('//select[contains(@class, "search-dropdown")]')

    def search_option(self, name):
        return self.driver.find_element_by_xpath(f'//option[contains(@value, "search-alias") and contains(text(), "{name}")]')

    def is_search_dd_option_selected(self, name):
        try:
            self.wait_for_element_text('//option[@selected="selected"]', name)
            return True
        except TimeoutException:
            return False

    def select_search_option(self, name):
        """Select Search drop down option by name
        :param name: Option name to be selected
        :return: Raise Exception is drop down menu not displayed
        """
        self.search_dropdown.click()
        if self.search_dd_menu.is_enabled():
            self.search_option(name).click()
        else:
            raise Exception('Search drop down menu not displayed')

    @property
    def books_page_title(self):
        el_xpath = '//img[@alt="Books at Amazon"]'
        self.wait_for_element_visibility(xpath=el_xpath)
        return self.driver.find_element_by_xpath(el_xpath)

    @property
    def sign_in_page_title(self):
        el_xpath = '//h1[contains(text(),  "Sign-In")]'
        self.wait_for_element_visibility(xpath=el_xpath)
        return self.driver.find_element_by_xpath(el_xpath)

    @property
    def childrens_books(self):
        el_xpath = '//div[contains(@data-value, "Children\'s Books")]'
        self.wait_for_element_visibility(xpath=el_xpath)
        return self.driver.find_element_by_xpath(el_xpath)

    def get_book_by_name(self, name):
        el_xpath = f'//span[contains(text(), "{name}")]'
        self.wait_for_element_visibility(xpath=el_xpath)
        return self.driver.find_element_by_xpath(el_xpath)

    @property
    def price(self):
        return self.driver.find_element_by_xpath('//span[@id="price"]')

    @property
    def add_to_card(self):
        return self.driver.find_element_by_xpath('//input[@id="add-to-cart-button"]')

    @property
    def items_in_the_card(self):
        return self.driver.find_element_by_xpath('//span[contains(@id, "nav-cart-count")]')

    @property
    def card_subtotal(self):
        el_xpath = '//span[contains(@*, "subtotal-amount")]//span'
        self.wait_for_element_visibility(xpath=el_xpath)
        return self.driver.find_element_by_xpath(el_xpath)

    @property
    def subtotal_label(self):
        return self.driver.find_element_by_xpath('//span[contains(@*, "sc-subtotal-label")]')

    def filter_by(self, name):
        el_xpath = f'//*[@aria-label="{name}"]'
        self.wait_for_element_visibility(xpath=el_xpath)
        return self.driver.find_element_by_xpath(el_xpath)

    @property
    def card_page_title(self):
        el_xpath = '//h1[contains(text(), "Shopping Cart")]'
        self.wait_for_element_visibility(xpath=el_xpath)
        return self.driver.find_element_by_xpath(el_xpath)

    @property
    def card_items(self):
        """Get all added to card items
        :return: List of added to card items names
        """
        el_xpath = '//span[contains(@class, "sc-product-title")]'
        self.wait_for_any_elements_visibility(xpath=el_xpath)
        items = self.driver.find_elements_by_xpath(el_xpath)
        items_names = [item.text for item in items]
        return items_names

    def get_card_item_by_name(self, name):
        return CardItem(self.driver, f'//div[@class="sc-list-item-content"][.//span[contains(text(), "{name}")]]')

    @property
    def active_card_subtotal(self):
        return self.driver.find_element_by_xpath('//span[contains(@id, "sc-subtotal-amount-activecart")]/span')

    @property
    def proceed_to_checkout(self):
        return self.driver.find_element_by_xpath('//input[@name="proceedToRetailCheckout"]')


