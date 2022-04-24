import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PATH_CHROME = 'C:\\Users\\user\\.wdm\\drivers\\chromedriver\\win32\\100.0.4896.60\\chromedriver.exe'
PATH_FIREFOX = 'C:\\Users\\user\\.wdm\\drivers\\geckodriver\\win64\\v0.30.0\\geckodriver.exe'


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose a language.")


@pytest.fixture(scope='session')
def browser(request):
    """Simple pre-initialization the Chrome/Firefox webdriver."""

    user_language: str = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)

    browser_name: str = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=PATH_CHROME,
                                  options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=PATH_FIREFOX,
                                   firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
