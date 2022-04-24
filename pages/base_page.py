class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self) -> None:
        self.browser.get(url=self.url)
