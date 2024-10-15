import json
import time

import allure
import pytest

from src.PageObject.Pages.LoginPlataformaPage2 import LoginPlataformaPage


@pytest.fixture(scope="class")
def antes_todos(self):
    print("antes de todos")
    self.login_plataforma_page = LoginPlataformaPage(self.driver)


@pytest.fixture(scope="function")
def antes_test(self):
    print("Inicializar el metodo")
    self.login_plataforma_page.inicializar()


@pytest.fixture(scope="class")
def despues_todos(self):
    yield
    print("Inicializar el metodo")
    self.driver.quit()


# Fixture para cargar la configuracion del ambiente desde el archivo json

# Añadir opcion --env a pytest para elegir el ambiente
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Seleccionar el ambiente de ejecucion")

@pytest.mark.usefixtures("setup")
class TestLoginPlataforma:

    #Para acceder a la configuracion en todas las pruebas
    @pytest.fixture(scope="class")
    def login_plataforma(self, config, setup):
        self.base_url = config["base_url"]
        login_plataforma = LoginPlataformaPage(setup, self.base_url)
        print("Setup login")
        return login_plataforma

    @allure.title("Campo tenant ok")
    @allure.description("Este test verifica que se encuentra el campo")
    def test_campo_tenant_ok(self, login_plataforma):
        # declaracion
        # self.driver.get(LoginPlataformaPage.get_base_url())

        # Ejecución
        resultado = login_plataforma.getTenantInput()

        # comprobacion
        texto_tenant_esperado = 'Nombre de espacio de trabajo *'
        assert texto_tenant_esperado in resultado.get_attribute('placeholder')

    @allure.title("Campo usuario ok")
    @allure.description("Este test verifica que se encuentra el campo")
    def test_02_campo_nombre_usurio_ok(self, login_plataforma):
        # declaracion
        #login_plataforma = LoginPlataformaPage(self.driver)
        # Ejecución
        resultado = login_plataforma.getUserNameInput()

        # comprobacion
        texto_usuario_esperado = 'Nombre de usuario o email *'
        assert texto_usuario_esperado in resultado.get_attribute('placeholder')

    @allure.title("Campo password ok")
    @allure.description("Este test verifica que se encuentra el campo")
    def test_03_campo_password_ok(self):
        # declaracion
        login_plataforma = LoginPlataformaPage(self.driver)
        # Ejecución
        resultado = login_plataforma.getPasswordInput()
        # comprobacion
        texto_contrasena_esperado = 'Contraseña *'
        assert texto_contrasena_esperado in resultado.get_attribute('placeholder')

    @allure.title("Check box recuerdame existe")
    @allure.description("Este test verifica que se encuentra el campo")
    def test_04_checkRecuerdame_ok(self):
        # declaracion
        login_plataforma = LoginPlataformaPage(self.driver)
        # Ejecución
        resultado = login_plataforma.getRecuerdameCheckBox()
        resultado_label = login_plataforma.getRecuerdameLabelCheckBox()

        # comprobacion
        label_recerdame_esperado = "Recuérdame"
        # Realizar un assert para comprobar que el checkbox fue encontrado y es visible
        # print("Resultado:", resultado, " Label:  ", resultado_label)
        assert resultado is not None, "El checkbox no se encontró."
        assert resultado.is_enabled(), "El checkbox no está habilitado en pantalla."
        assert label_recerdame_esperado in resultado_label.text

    @allure.title("Boton olvido clave existe")
    @allure.description("Este test verifica que se encuentra el link con el texto correcto")
    def test_05_ButtonOlvidoContrasena_ok(self):
        # declaracion
        login_plataforma = LoginPlataformaPage(self.driver)
        # Ejecución
        resultado_link_text = login_plataforma.getOlvidoPassLink().text
        resultado_button = login_plataforma.getOlvidoPassLinkButton()

        # comprobacion
        text_OlvidoPass_esperado = "Olvidó la contraseña?"
        # Realizar un assert para comprobar que el link tiene el texto y esta visible y  habilitado para clic
        assert text_OlvidoPass_esperado in resultado_link_text
        assert resultado_button.is_displayed(), "El link no esta visible"
        assert resultado_button.is_enabled(), "El link no esta habilitado para click"

    @allure.title("Boton olvido tenant existe")
    @allure.description("Este test verifica que se encuentra el link con el texto correcto")
    def test_06_ButtonOlvidoTenant_ok(self):
        # declaracion
        login_plataforma = LoginPlataformaPage(self.driver)
        # Ejecución
        resultado_link_text = login_plataforma.getOlvidoTenantLink().text
        resultado_button = login_plataforma.getOlvidoTenantLinkButton()

        # comprobacion
        text_OlvidoTenant_esperado = "Olvidó su espacio de trabajo?"
        # Realizar un assert para comprobar que el link tiene el texto y esta visible y  habilitado para clic
        assert text_OlvidoTenant_esperado in resultado_link_text
        assert resultado_button.is_displayed(), "El link no esta visible"
        assert resultado_button.is_enabled(), "El link no esta habilitado para click"

    @allure.title("Login correcto")
    @allure.description("Este test verifica que se hace el login con los datos correctos")
    def test_07_LoginPlataformaOK(self):
        # declaracion
        tenan = "Agenda22022022"
        usuario = "Andreina"
        clave = "123qwe"
        login_plataforma = LoginPlataformaPage(self.driver)

        # ejecucion
        login_plataforma.login(tenan, usuario, clave)

        # comprobacion
        tenanEsperado = "Agenda22022022"
        usuarioEsperado = "Andreina"
        assert tenanEsperado in login_plataforma.getTenantLoginOK().text
        assert usuarioEsperado in login_plataforma.getUsuarioLoginOK().text

    @allure.title("Log incorrecto usurio o clave no son validas")
    @allure.description("Este test verifica que no se puede loguear con datos usuarioclasve no validos")
    def test_08_LoginPlataformaERROR_UsuarioClave(self):
        # declaracion
        tenan = "Agenda22022022"
        usuario = "Andre"
        clave = "12qw"
        login_plataforma = LoginPlataformaPage(self.driver)
        time.sleep(3)

        # ejecucion
        login_plataforma.login(tenan, usuario, clave)
        time.sleep(5)

        # comprobacion
        TitleEsperado = "Inicio de sesión fallido!"
        MsgEsperado = "Nombre de usuario o contraseña incorrecta"

        assert TitleEsperado in login_plataforma.getError_Login_title().text
        assert MsgEsperado in login_plataforma.getError_Login_Msg().text

        # Paso2 Cerrar PopUp de mensaje de error
        login_plataforma.getErrorLoginButton().click()

    @allure.title("Log incorrecto Tenant no existe")
    @allure.description("Este test verifica que no se puede loguear en un tenant que no existe")
    def test_09_LoginPlataformaERROR_Tenant(self):
        # declaracion
        tenan = "Agenda220220"
        usuario = "Andreina"
        clave = "123qwe"
        login_plataforma = LoginPlataformaPage(self.driver)

        # ejecucion
        login_plataforma.login(tenan, usuario, clave)

        # comprobacion
        MsgEsperado = "No existe un Espacio de Trabajo con nombre Agenda220220"
        assert MsgEsperado in login_plataforma.getError_Login_TenantMsg().text

        # Paso2 Cerrar PopUp de mensaje de error
        login_plataforma.getErrorLoginButton().click()


