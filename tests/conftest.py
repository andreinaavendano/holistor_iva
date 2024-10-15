import json

import allure
import pytest
from allure_commons.types import AttachmentType

from utils.driver_factory import DriverFactory


CONFIG_PATH = "config_prod.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]
DEFAULT_URL = "https://plataforma-saas-qa.azurewebsites.net"
#DEFAULT_URL = "https://holistorsaas.com.ar/account/login"

@pytest.fixture(scope="session")
def config(request):
    print("request config", request.config)
    env = request.config.inicfg["env"]
    with open(f"F:\Projects\Selenium\SeleniumPython\pythonProjectHolistorIVAWeb\config_{env}.json") as config_file:
        config_data = json.load(config_file)

    return config_data



@pytest.fixture(scope="session")
def browser_setup(config):
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


@pytest.fixture(scope='session')
def wait_time_setup(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def url_setup(config):
    return config["base_url"] if "base_url" in config else DEFAULT_URL


@pytest.fixture(scope='session')
def setup(request, config):
    driver = DriverFactory.get_driver(config)
    driver.implicitly_wait(config["timeout"])
    return driver


def nada():
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    if config["browser"] == "firefox":
        driver.maximize_window()
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()
