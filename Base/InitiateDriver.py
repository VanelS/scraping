from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from Libraries.ConfigReader import Config


class Browser:

    path = "../Drivers/geckodriver"
    driver = None

    @classmethod
    def startBrowser(cls):

        browser = Config.read_config_data('Details', 'Browser')
        os = Config.read_config_data('Details', 'OS')

        if browser == "Firefox" and os == 'Linux':
            path = "../Drivers/geckodriver"
            driver = Firefox(executable_path=path)
        elif browser == "Chrome" and os == 'Linux':
            path = "../Drivers/chromedriver"
            driver = Chrome(executable_path=path)
        else:
            raise Exception("Browser not supported")

        return cls.driver

    @classmethod
    def closeBrowser(cls):
        cls.driver.close()

