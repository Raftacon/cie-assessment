import unittest
from locators import *

class BasePage():
	def __init__(self, driver):
		self.driver = driver
		self.driver.implicitly_wait(5)
		self.timeout = 15

	def set_field(self, locator, text):
		field = self.driver.find_element(*locator)
		field.send_keys(text)

	def click_button(self, locator):
		button = self.driver.find_element(*locator)
		button.click()

	def assert_text_match(self, locator, text):
		element = self.driver.find_element(*locator)
		assert (element.text == text), \
			(f'\nElement value:\t"{element.text}"\nDesired text:\t"{text}"')