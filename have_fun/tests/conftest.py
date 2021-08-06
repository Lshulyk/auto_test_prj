import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from have_fun.page_objects.amazon import AmazonPage
from have_fun.page_objects.herokuapp import HerokuappPage, HerokuappChallengingDomPage


@pytest.fixture(scope='module')
def chrome_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install(), service_args=["--verbose", "--log-path=chrome_browser.log"])
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def firefox_browser():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def herokuapp_page(firefox_browser):
    firefox_browser.get("http://the-internet.herokuapp.com/")
    return HerokuappPage(firefox_browser)


@pytest.fixture(scope='module')
def herokuapp_challenging_dom_page(firefox_browser):
    firefox_browser.get("http://the-internet.herokuapp.com/challenging_dom")
    return HerokuappChallengingDomPage(firefox_browser)


@pytest.fixture(scope='module')
def amazon_page(chrome_browser):
    chrome_browser.get("https://www.amazon.com/")
    return AmazonPage(chrome_browser)
