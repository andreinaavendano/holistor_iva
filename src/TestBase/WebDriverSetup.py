import unittest
from selenium import webdriver
import urllib3
import time


class WebDriverSetup(unittest.TestCase):

     #inicializar el web driver
    def setUp(self):
        #desactivar los warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        #crear el driver de chrome
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    #para cerrar el browser y ejecutar algun codgo mo reporteria
    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()


