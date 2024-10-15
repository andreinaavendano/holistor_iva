import time

import allure
import pytest

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.LoginPlataformaPage2 import LoginPlataformaPage
from src.PageObject.Pages.RecuperarClaveTenant import RecuperarClaveTenant
from utils.leer_xlsx import leer_xlsx

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Test_RecuperarClaveTenant:
    def test_01_campo_tenant_ok(self):
        # declaracion

        login_plataforma = LoginPlataformaPage(self.driver)
        time.sleep(3)

        # Ejecución
        resultado = login_plataforma.goOlvidoPassLinkButtonClic(self.driver)
        print("REsultado: ", resultado)
        time.sleep(20)

        pag_RecuperarClaveTenant = RecuperarClaveTenant(self.driver)
        resultado1 = pag_RecuperarClaveTenant.getTenantInput()
        print("REsultado1: ", resultado)

        # comprobacion
        texto_tenant_esperado = 'Nombre de espacio de trabajo *'
        assert texto_tenant_esperado in resultado1.get_attribute('placeholder')

    def test_02_campo_email_ok(self):
        # declaracion
        self.driver.get(LoginPlataformaPage.get_base_url())
        login_plataforma = LoginPlataformaPage(self.driver)
        time.sleep(3)

        # Ejecución
        login_plataforma.goOlvidoPassLinkButtonClic()
        time.sleep(3)

        pag_RecuperarClaveTenant = RecuperarClaveTenant(self.driver)
        resultado = pag_RecuperarClaveTenant.getEmailInput()

        # comprobacion
        texto_usuario_esperado = 'Dirección de email *'
        assert texto_usuario_esperado in resultado.get_attribute('placeholder')

    def test_03_enviar_button_ok(self):
        # declaracion
        self.driver.get(LoginPlataformaPage.get_base_url())
        login_plataforma = LoginPlataformaPage(self.driver)
        time.sleep(3)

        # Ejecución
        login_plataforma.goOlvidoPassLinkButtonClic()
        time.sleep(3)

        pag_RecuperarClaveTenant = RecuperarClaveTenant(self.driver)
        resultado = pag_RecuperarClaveTenant.getEnviarButton()

        # comprobacion
        text_boton_esperado = "Enviar"
        assert text_boton_esperado in resultado.text
        assert resultado.is_displayed(), "El botón no esta visible"
        assert not resultado.is_enabled(), "El botón esta habilitado para click"

    def test_04_atras_button_ok(self):
        # declaracion
        self.driver.get(LoginPlataformaPage.get_base_url())
        login_plataforma = LoginPlataformaPage(self.driver)
        time.sleep(3)

        # Ejecución
        login_plataforma.goOlvidoPassLinkButtonClic()
        time.sleep(3)

        pag_RecuperarClaveTenant = RecuperarClaveTenant(self.driver)
        resultado = pag_RecuperarClaveTenant.getAtrasButton()

        # comprobacion
        text_boton_esperado = "Atrás"
        assert text_boton_esperado in resultado.text
        assert resultado.is_displayed(), "El botón no esta visible"
        assert resultado.is_enabled(), "El botón no esta habilitado para click"

    def test_05_TenantNoValido(self):
        # declaracion
        self.driver.get(LoginPlataformaPage.get_base_url())
        login_plataforma = LoginPlataformaPage(self.driver)
        time.sleep(3)

        tenant = "novalido"
        email = "aavendano@holistor.com.ar"

        # Ejecución
        login_plataforma.goOlvidoPassLinkButtonClic()
        time.sleep(3)

        pag_RecuperarClaveTenant = RecuperarClaveTenant(self.driver)
        pag_RecuperarClaveTenant.setInputDatos(tenant, email)
        pag_RecuperarClaveTenant.goEnviarButton()

        resultado = pag_RecuperarClaveTenant.getError_Tenant_Email_Novalido_Msg().text

        # comprobacion
        text_esperado = "No existe un Espacio de Trabajo con nombre novalido"
        assert text_esperado in resultado

    def test_06_EmailNoValido(self):
        # declaracion
        self.driver.get(LoginPlataformaPage.get_base_url())
        login_plataforma = LoginPlataformaPage(self.driver)
        time.sleep(3)

        tenant = "espaciosoporte"
        email = "aavendano@holistor.com"

        # Ejecución
        login_plataforma.goOlvidoPassLinkButtonClic()
        time.sleep(3)

        pag_RecuperarClaveTenant = RecuperarClaveTenant(self.driver)
        pag_RecuperarClaveTenant.setInputDatos(tenant, email)
        pag_RecuperarClaveTenant.goEnviarButton()

        resultado = pag_RecuperarClaveTenant.getError_Tenant_Email_Novalido_Msg().text

        # comprobacion
        text_esperado = "Dirección de correo inválida"
        assert text_esperado in resultado

    def test_07_DatosValidos(self):
        # declaracion
        self.driver.get(LoginPlataformaPage.get_base_url())
        login_plataforma = LoginPlataformaPage(self.driver)
        time.sleep(3)

        tenant = "espaciosoporte"
        email = "aavendano@holistor.com.ar"

        # Ejecución
        login_plataforma.goOlvidoPassLinkButtonClic()
        time.sleep(3)

        pag_RecuperarClaveTenant = RecuperarClaveTenant(self.driver)
        pag_RecuperarClaveTenant.setInputDatos(tenant, email)
        pag_RecuperarClaveTenant.goEnviarButton()

        resultado = pag_RecuperarClaveTenant.getError_Tenant_Email_Novalido_Msg().text

        # comprobacion
        text_esperado = "Correo enviado"
        assert text_esperado in resultado

    def test_08_Accion_Atras_Ok(self):
        # declaracion
        self.driver.get(LoginPlataformaPage.get_base_url())
        login_plataforma = LoginPlataformaPage(self.driver)
        time.sleep(3)

        tenant = "espaciosoporte"
        email = "aavendano@holistor.com.ar"

        # Ejecución
        login_plataforma.goOlvidoPassLinkButtonClic()
        time.sleep(3)

        pag_RecuperarClaveTenant = RecuperarClaveTenant(self.driver)
        pag_RecuperarClaveTenant.setInputDatos(tenant, email)
        pag_RecuperarClaveTenant.goAtrasButton()

        url_resultado = self.driver.current_url

        # comprobacion
        assert LoginPlataformaPage.get_base_url() in url_resultado

    @allure.title("Search flight test: one way")
    @allure.description("This is test of searching one way flight")
    @pytest.mark.parametrize("datos", leer_xlsx.get_xlsx_olvidoClave_data())
    def test_09_OlvidoClaveDatos(self, datos):
        print("datos", datos)
        # declaracion
        self.driver.get(LoginPlataformaPage.get_base_url())
        login_plataforma = LoginPlataformaPage(self.driver)
        time.sleep(3)

        # Ejecución
        login_plataforma.goOlvidoPassLinkButtonClic()
        time.sleep(3)
        pag_RecuperarClaveTenant = RecuperarClaveTenant(self.driver)
        pag_RecuperarClaveTenant.setInputTenant(datos.tenant)
        pag_RecuperarClaveTenant.setInputEmail(datos.email)
        resultado = pag_RecuperarClaveTenant.goEnviarButton()

        # comprobacion
        assert not resultado.is_enabled(), "El botón esta habilitado para click"
