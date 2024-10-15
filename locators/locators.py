from selenium.webdriver.common.by import By


class LogInPlataformaLocators:
    TENANT_BOX = (By.NAME, "tenancyName")
    USERNAME_BOX = (By.NAME, "userNameOrEmailAddress")
    PASSWORD_BOX = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='kt_login']/div/div[2]/div[2]/ng-component/div/form/div[5]/div[2]/button")
    #RECUERDAME_CHEKBOX = (By.NAME, "rememberMe")
    # Localizar el checkbox y hacer click
    RECUERDAME_CHEKBOX = (By.NAME, "rememberMe")
    RECUERDAME_LABEL = (By.XPATH, "//label[contains(., 'Recuérdame')]")

    # Localizadores de los enlaces de recuperación Password
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Olvidó la contraseña?")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//*[@id='forget-password']")

    # Localizadores de los enlaces de recuperación Tenant
    FORGOT_TENANT_LINK = (By.LINK_TEXT, "Olvidó su espacio de trabajo?")
    FORGOT_TENANT_BUTTON = (By.XPATH, "//*[@id='forget-password']")

    # Localizador que indica que la página de login ha cargado
    TENAN_TEXTO = (By.XPATH, "//*[@id='kt_header']/topbar/div/div[3]/div/div/span/span")
    USUARIO_TEXTO = (By.XPATH, "//*[@id='kt_header']/topbar/div/div[3]/div/div/span")

    #Localizadores de Credenciales Incorrectas
    ERROR_LOGIN_TITLE = (By.XPATH, "// *[@id = 'swal2-title']")
    ERROR_LOGIN_MSG = (By.XPATH, "// *[@id = 'swal2-content']")
    ERROR_LOGIN_BUTTON = (By.XPATH, "/html/body/div/div/div[3]/button[1]")

    #Localizadores de Tenant No existe
    ERROR_LOGIN_TENANT_MSG = (By.XPATH, "//*[@id = 'swal2-title']")

class ForgotpasswordLocators:
    #Localizadores Olvido Contraseña
    #TENANT_BOX = (By.XPATH, "//*[@id = 'kt_login']/div/div[2]/div[2]/ng - component/div/form/div[1]/input")
    TENANT_BOX = (By.NAME, "tenancyName")
    #EMAIL_BOX = (By.XPATH,  "//*[@id='kt_login']/div/div[2]/div[2]/ng-component/div/form/div[2]/input")
    EMAIL_BOX = (By.NAME, "emailAddress")
    ENVIAR_BUTTON = (By.XPATH, "//*[@id='kt_login']/div/div[2]/div[2]/ng-component/div/form/div[3]/button[2]")
    ATRAS_BUTTON = (By.XPATH, "//*[@id='kt_login']/div/div[2]/div[2]/ng-component/div/form/div[3]/button[1]")
    # Localizadores de Tenant No existe
    ERROR_MSG = (By.XPATH, "//*[@id = 'swal2-title']")


