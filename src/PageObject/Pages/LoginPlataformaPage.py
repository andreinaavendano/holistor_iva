import time

from selenium.webdriver.common.by import By

from locators import LogInPlataformaLocators

base_url = "https://plataforma-saas-qa.azurewebsites.net/account/login"

class LoginPlataformaPage:

    def get_base_url():
        return base_url
    def __init__(self, driver):
        self.driver = driver
        self.ByTenantBoxLocator = "tenancyName"
        self.ByusernameBoxLocator = "userNameOrEmailAddress"
        self.BypasswordBoxLocator = "password"
        self.ByloginBtnLocator = "//*[@id='kt_login']/div/div[2]/div[2]/ng-component/div/form/div[5]/div[2]/button"
        # Localizador que indica que la pagina login cargo
        self.BypageLoginLocator = "//*[@id='kt_header']/topbar/div/div[3]/div/div/span/span"
        # Localizador de los links
        self.ByOlvidoPass ="Olvidó la contraseña?"
        self.ByOlvidoTenant = "Olvidó su espacio de trabajo?"
        self.BysyjAplicacion = "//img[@src='/assets/common/images/holistor/SYJ-logo.png']" #logo APP SYJ


    def getTenantImput(self):
        return self.driver.find_element(*LogInPlataformaLocators.ByTenantBoxLocatorName)

    def getUserNameImput(self):
        return self.driver.find_element(*LogInPlataformaLocators.ByusernameBoxLocatorName)

    def getpasswordImput(self):
        return self.driver.find_element(*LogInPlataformaLocators.BypasswordBoxLocatorName)

    def getLoginButton(self):
        return self.driver.find_element(*LogInPlataformaLocators.ByloginBtnLocatorXPath)

    def getBypageLogin(self):
        return self.driver.find_element(*LogInPlataformaLocators.BypageLoginLocatorXPath)

    def getByOlvidoPassLink(self):
        return self.driver.find_element(*LogInPlataformaLocators.ByOlvidoPassLinkText)

    def getByOlvidoTenantLink(self):
        return self.driver.find_element(*LogInPlataformaLocators.ByOlvidoTenantLinkText)

    def getLBysyjAplicacion(self):
        return self.driver.find_element(By.NAME, self.BysyjAplicacion)

    def isTenantDisplay(self):
       return self.driver.find_element(self.ByTenantBoxLocator)

    def set_user_inputs(self, tenant, usuario, clave):
        #limpia los text imput
        print(tenant, usuario, clave)

        self.getTenantImput().send_keys("")
        self.getUserNameImput().send_keys("")
        self.getpasswordImput().send_keys("")

        self.getTenantImput().send_keys(tenant)
        time.sleep(3)
        self.getUserNameImput().send_keys(usuario)
        time.sleep(3)
        self.getpasswordImput().send_keys(clave)
        time.sleep(3)

    def buttonClicLogin(self):
        self.getLoginButton().click()