from selenium.webdriver.common.by import By

class LoginPageLocators():
	LOGIN_EMAIL_FIELD = (By.ID, 'login-email-field')
	LOGIN_PASSWORD_FIELD = (By.ID, 'login-password-field')
	LOGIN_BUTTON = (By.ID, 'login-login-button')
	RESULT_NOTIFICATION = (By.CLASS_NAME, 'notification')