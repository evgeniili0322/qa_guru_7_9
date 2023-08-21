import pytest
from selenium import webdriver
from selene import browser

options = webdriver.ChromeOptions()


@pytest.fixture(scope='function')
def browser_opt():
    # options.add_argument('--headless')
    options.add_argument('window_size=1920,1080')
    browser.config.driver_options = options
    browser.config.base_url = 'https://github.com'

    yield

    browser.quit()
