from msedge.selenium_tools import EdgeOptions, Edge
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from extensions.webdriver_extended import WebDriverExtended
from helpers.webdriver_listener import WebDriverListener


class DriverFactory:
    @staticmethod
    def get_driver(config) -> WebDriverExtended:
        if config["browser"] == "chrome":
            options = webdriver.Chrome()#webdriver.ChromeOptions()
            options.maximize_window()
            options.implicitly_wait(config["timeout"])
            driver = WebDriverExtended(
                options,
                WebDriverListener(), config
            )
            return driver
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            if config["headless_mode"] is True:
                options.headless = True
            driver = WebDriverExtended(
                webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options),
                WebDriverListener(), config
            )
            return driver
        elif config["browser"] == "edge":
            options = EdgeOptions()
            options.use_chromium = True
            if config["headless_mode"] is True:
                options.headless = True
            driver_path = EdgeChromiumDriverManager().install()
            driver = WebDriverExtended(
                Edge(executable_path=driver_path, options=options),
                WebDriverListener(), config
            )
            return driver
        raise Exception("Provide valid driver name")
