from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, text_to_be_present_in_element, \
    visibility_of_any_elements_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def page_url(self):
        return self.driver.current_url

    def get_web_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def wait_for_element_visibility(self, xpath, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(visibility_of_element_located((By.XPATH, xpath)))
        except StaleElementReferenceException:
            # need to add small timeout 1 second is case of StaleElementReferenceException
            time.sleep(1)
            wait.until(visibility_of_element_located((By.XPATH, xpath)))

    def wait_for_any_elements_visibility(self, xpath, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(visibility_of_any_elements_located((By.XPATH, xpath)))
        except StaleElementReferenceException:
            # need to add small timeout 1 second is case of StaleElementReferenceException
            time.sleep(1)
            wait.until(visibility_of_any_elements_located((By.XPATH, xpath)))

    def wait_for_element_text(self, xpath, text, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(text_to_be_present_in_element((By.XPATH, xpath), text))
        except StaleElementReferenceException:
            # need to add small timeout 1 second is case of StaleElementReferenceException
            time.sleep(1)
            wait.until(text_to_be_present_in_element((By.XPATH, xpath), text))

    def wait_for_element_enabled(self, xpath, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(element_to_be_clickable((By.XPATH, xpath)))
        except StaleElementReferenceException:
            # need to add small timeout 1 second is case of StaleElementReferenceException
            time.sleep(1)
            wait.until(element_to_be_clickable((By.XPATH, xpath)))