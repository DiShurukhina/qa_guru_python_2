import pytest
from selene.support.shared import browser, config


@pytest.fixture()
def open_browser():
    config.window_height = 1080
    config.window_width = 1920
#   config.browser_name = 'firefox'
    browser.open('https://google.com/ncr')
    yield