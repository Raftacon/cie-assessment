import os
import glob
import unittest
from tests.test_login import LoginPageTests

# Initial run setup:
if not os.path.exists("screenshots/"):
	os.makedirs("screenshots/")

# Compile test suite of tests to run:
login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginPageTests)
test_suite = unittest.TestSuite(login_tests)

# Clear any pre-existing screenshots from the last suite run:
files = glob.glob("screenshots/*")

for file in files:
	os.remove(file)

unittest.TextTestRunner().run(test_suite)