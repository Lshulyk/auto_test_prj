from have_fun.page_objects.base_page import BasePage


class DropDown(BasePage):
    def __init__(self, driver, xpath):
        self.driver = driver
        self.xpath = xpath
        self.myself = self.get_web_element_by_xpath(self.xpath)

    def get_option(self, name):
        xpath=f'//option[text()="{name}"]'
        self.wait_for_element_visibility(xpath)
        return self.get_web_element_by_xpath(xpath)

    def select_option(self, name):
        self.myself.click()
        self.get_option(name).click()

    @property
    def current_option(self):
        return self.get_web_element_by_xpath('//option[@selected="selected"]')


class HerokuappPage(BasePage):

    @property
    def drop_down_label(self):
        return self.get_web_element_by_xpath('//a[contains(text(), "Dropdown")]')

    @property
    def drop_down_list_page_title(self):
        xpath = '//*[contains(text(), "Dropdown List")]'
        self.wait_for_element_visibility(xpath)
        return self.get_web_element_by_xpath(xpath)

    @property
    def drop_down(self):
        return DropDown(self.driver, xpath='//select[@id="dropdown"]')


class Row(BasePage):
    def __init__(self, driver, xpath):
        self.driver = driver
        self.xpath = xpath

    @property
    def delete(self):
        xpath = f'{self.xpath}//a[text()="delete"]'
        return self.get_web_element_by_xpath(xpath)


class HerokuappChallengingDomPage(BasePage):

    @property
    def button(self):
        return self.get_web_element_by_xpath('//a[@class="button"]')

    @property
    def success_button(self):
        return self.get_web_element_by_xpath('//a[@class="button success"]')

    @property
    def alert_button(self):
        return self.get_web_element_by_xpath('//a[@class="button alert"]')

    def get_label_by_name(self, name):
        """Get page lable by name
        :param name: String label name
        :return: WebElement object of label
        """
        xpath = f'//*[text()="{name}"]'
        return self.get_web_element_by_xpath(xpath)

    def get_row_by_index(self, index):
        """Get table row by index
        :param index: Integer row index
        :return: Row class instance
        """
        # Increase row index to 1 because first row is columns names
        index = index + 1
        return Row(self.driver, xpath=f'(//tr)[{index}]')
