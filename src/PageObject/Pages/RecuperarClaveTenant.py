from src.PageObject.Pages.LoginPlataformaPage2 import LoginPlataformaPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import ForgotpasswordLocators

TIMEOUT = 10

#base_url = "https://plataforma-saas-qa.azurewebsites.net/account/login"
#base_url = "https://holistorsaas.com.ar/account/login"

class RecuperarClaveTenant:


    def __init__(self, driver):
        self.driver = driver

    def getTenantInput(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(ForgotpasswordLocators.TENANT_BOX)
        )

    def getEmailInput(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(ForgotpasswordLocators.EMAIL_BOX)
        )

    def getEnviarButton(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(ForgotpasswordLocators.ENVIAR_BUTTON)
        )

    def goEnviarButton(self):
        return self.getEnviarButton().click()


    def getAtrasButton(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(ForgotpasswordLocators.ATRAS_BUTTON)
        )

    def goAtrasButton(self):
        return self.getAtrasButton().click()

    def setInputDatos(self, tenant, email):
        # Limpia los campos de texto
        self.getTenantInput().clear()
        self.getEmailInput().clear()

        # Introduce los datos requeridos para recuperar la contraseña
        self.getTenantInput().send_keys(tenant)
        self.getEmailInput().send_keys(email)

    def setInputTenant(self, tenant):
        # Limpia los campos de texto
        self.getTenantInput().clear()

        # Introduce los datos requeridos para recuperar la contraseña
        self.getTenantInput().send_keys(tenant)

    def setInputEmail(self, email):
        # Limpia los campos de texto
        self.getEmailInput().clear()

        # Introduce los datos requeridos para recuperar la contraseña
        self.getEmailInput().send_keys(email)

    def getError_Tenant_Email_Novalido_Msg(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(ForgotpasswordLocators.ERROR_MSG)
        )


