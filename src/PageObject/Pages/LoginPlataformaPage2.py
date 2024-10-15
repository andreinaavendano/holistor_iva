import json
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from extensions.webdriver_extended import WebDriverExtended
from locators.locators import LogInPlataformaLocators
from utils.driver_factory import DriverFactory

TIMEOUT = 10

#base_url = "https://plataforma-saas-qa.azurewebsites.net/account/login"
#base_url = "https://holistorsaas.com.ar/account/login"


class LoginPlataformaPage:

    def __init__(self, driver: WebDriverExtended, base_url):
        self.driver = driver
        self.base = base_url
        self.login_page = "/account/login"
        self.inicializar()

    def inicializar(self):
        self.driver.get(self.base + self.login_page)

    def getTenantInput(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(LogInPlataformaLocators.TENANT_BOX)
        )

    def getUserNameInput(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(LogInPlataformaLocators.USERNAME_BOX)
        )

    def getPasswordInput(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(LogInPlataformaLocators.PASSWORD_BOX)
        )

    def getRecuerdameCheckBox(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(LogInPlataformaLocators.RECUERDAME_CHEKBOX)
        )

    def getRecuerdameLabelCheckBox(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(LogInPlataformaLocators.RECUERDAME_LABEL)
        )

    def getLoginButton(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(LogInPlataformaLocators.LOGIN_BUTTON)
        )

    def getOlvidoPassLink(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(LogInPlataformaLocators.FORGOT_PASSWORD_LINK)
        )

    def getOlvidoPassLinkButton(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(LogInPlataformaLocators.FORGOT_PASSWORD_BUTTON)
        )


    def goOlvidoPassLinkButtonClic(self):
        resul = self.getOlvidoPassLinkButton()
        print("RESULTADO: ", resul)
        return resul
        #return self.getOlvidoPassLinkButton().click()

    def getOlvidoTenantLink(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(LogInPlataformaLocators.FORGOT_TENANT_LINK)
        )

    def getOlvidoTenantLinkButton(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(LogInPlataformaLocators.FORGOT_TENANT_BUTTON)
        )

    def gotOlvidoTenantLinkButtonClic(self):
        return self.getOlvidoTenantLinkButton().click()


    def getTenantLoginOK(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(LogInPlataformaLocators.TENAN_TEXTO)
        )

    def getUsuarioLoginOK(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(LogInPlataformaLocators.USUARIO_TEXTO)
        )

    def getError_Login_title(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(LogInPlataformaLocators.ERROR_LOGIN_TITLE)
        )

    def getError_Login_Msg(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(LogInPlataformaLocators.ERROR_LOGIN_MSG)
        )
    def getErrorLoginButton(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(LogInPlataformaLocators.ERROR_LOGIN_BUTTON)
        )

    def getError_Login_TenantMsg(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(LogInPlataformaLocators.ERROR_LOGIN_TENANT_MSG)
        )
    """def getLogoSYJAplicacion(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.BysyjAplicacion))
        )"""



    def set_user_inputs(self, tenant, usuario, clave):
        # Limpia los campos de texto
        self.getTenantInput().clear()
        self.getUserNameInput().clear()
        self.getPasswordInput().clear()

        # Introduce los datos de usuario
        self.getTenantInput().send_keys(tenant)
        self.getUserNameInput().send_keys(usuario)
        self.getPasswordInput().send_keys(clave)

    def buttonClickLogin(self):
        self.getLoginButton().click()

    def login(self, tenant, usuario, clave):
        self.set_user_inputs(tenant, usuario, clave)
        self.buttonClickLogin()

    #def logout(self):
        # click en el nombre
        # click en salir



