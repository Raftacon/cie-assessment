<p align="center">
  <img src="sample.PNG">
</p>

# Overview

This is a very basic configuration with minimal extra libraries to help demonstrate the valid login scenario from the technical assessment (—as well as some additional cases, like test cases from the manual part of the assessment & an example of an assertion failure.)

A quick reproduction of the screen from the manual assessment can be found [here](https://raftacon.io/cie/) and is used as the destination for the end-to-end testing in this repo. (The manual part of this assessment can also be found as a PDF in the `manual` subfolder.)

## Assumption

* `chromedriver` for your local version of Chrome is already installed & added to **PATH**.

## Usage

A test run can be observed by pulling down the repo & running:

```python -m suites.login_suite```


At the start of each run, the **screenshots** folder is scrubbed in preparation of the next suite execution. After each test case, a screenshot of the test case result is taken as part of the `tearDown` step.

Some sample output (including the intentional-fail test case):

```python
======================================================================
FAIL: test_wrong_notification_message_displayed (tests.test_login.SignInPageTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Raftacon\Desktop\cie\tests\test_login.py", line 50, in test_wrong_notification_message_displayed
    self.page.assert_notification_text(TestData.NOTIFICATION_TEXT_SUCCESS)
  File "C:\Users\Raftacon\Desktop\cie\pages.py", line 35, in assert_notification_text
    self.assert_text_match(SignInPageLocators.RESULT_NOTIFICATION, text)
  File "C:\Users\Raftacon\Desktop\cie\pages.py", line 20, in assert_text_match
    assert (element.text == text), \
AssertionError:
Element value:  "Login failed, please try again."
Desired text:   "Login successful!"

----------------------------------------------------------------------
Ran 6 tests in 30.450s

FAILED (failures=1)
```

## Future Improvements:
* Implement configuration to easily cycle Selenium targets between Chrome, Firefox, etc.
* Either roll on template or find a better library to prettify results.