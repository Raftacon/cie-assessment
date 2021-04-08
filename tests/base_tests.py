import unittest
from selenium import webdriver
from pages.login_page import LoginPage

class BaseTest(unittest.TestCase):
	def setUp(self):
		options = webdriver.ChromeOptions()
		options.add_argument('--start-maximized')

		self.driver = webdriver.Chrome(options=options)
		self.driver.get("https://raftacon.io/cie")

	def tearDown(self):
		self.driver.save_screenshot(f"screenshots/{self._testMethodName}.png")
		self.driver.quit()


class LoginBaseTest(BaseTest):
	def setUp(self):
		super().setUp()
		self.page = LoginPage(self.driver)