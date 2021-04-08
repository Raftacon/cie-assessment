import unittest
from selenium import webdriver
from .base_tests import LoginBaseTest
from data.login_test_data import LoginPageTestData as TestData

class LoginPageTests(LoginBaseTest):
	def test_successful_login(self):
		self.page.login(TestData.VALID_EMAIL, TestData.VALID_PASSWORD)
		self.page.assert_notification_text(TestData.NOTIFICATION_TEXT_SUCCESS)

	def test_no_email_address_provided(self):
		self.page.login(TestData.EMPTY_VALUE, TestData.STANDARD_PASSWORD)
		self.page.assert_notification_text(TestData.NOTIFICATION_TEXT_FAILURE)

	def test_no_password_provided(self):
		self.page.login(TestData.VALID_EMAIL, TestData.EMPTY_VALUE)
		self.page.assert_notification_text(TestData.NOTIFICATION_TEXT_FAILURE)

	def test_incomplete_email_address_provided(self):
		self.page.login(TestData.INCOMPLETE_EMAIL, TestData.STANDARD_PASSWORD)
		self.page.assert_notification_text(TestData.NOTIFICATION_TEXT_FAILURE)

	def test_unregistered_email_address_provided(self):
		self.page.login(TestData.UNREGISTERED_EMAIL, TestData.STANDARD_PASSWORD)
		self.page.assert_notification_text(TestData.NOTIFICATION_TEXT_FAILURE)

	# Intentional failing test case to illustrate
	# capturing assertion failure:
	def test_wrong_notification_message_displayed(self):
		self.page.login(TestData.UNREGISTERED_EMAIL, TestData.STANDARD_PASSWORD)
		self.page.assert_notification_text(TestData.NOTIFICATION_TEXT_SUCCESS)