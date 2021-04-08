import unittest
from locators.login_page_locators import LoginPageLocators
from .base_page import BasePage

class LoginPage(BasePage):
	def set_email(self, email):
		self.set_field(LoginPageLocators.LOGIN_EMAIL_FIELD, email)

	def set_password(self, password):
		self.set_field(LoginPageLocators.LOGIN_PASSWORD_FIELD, password)

	def click_login_button(self):
		self.click_button(LoginPageLocators.LOGIN_BUTTON)

	def assert_notification_text(self, text):
		self.assert_text_match(LoginPageLocators.RESULT_NOTIFICATION, text)

	def login(self, email, password):
		self.set_email(email)
		self.set_password(password)
		self.click_login_button()