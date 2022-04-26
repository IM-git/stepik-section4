import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

TIME = 4


def pytest_addoption(parser) -> None:
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose a language.")


@pytest.fixture(scope='function')
def browser(request):
    """Simple pre-initialization the Chrome/Firefox webdriver."""
    user_language: str = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs',
                                    {'intl.accept_languages': user_language})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    browser_name: str = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    driver.implicitly_wait(TIME)
    driver.maximize_window()
    yield driver
    driver.quit()
