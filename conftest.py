import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def open_browser():
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    #browser.config.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.driver.set_window_size(1920, 1080)
    browser.open('https://google.com/ncr')
    yield