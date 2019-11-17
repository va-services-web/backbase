from ui.base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from ui import ui_config as uc
from utilities.util import Util


class SignupPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _signup_link = '//a[@routerlink="/register"]'
    _login_link = '//a[@routerlink="/login"]'
    _home_link = '//a[@routerlink="/"]'

    _have_account_link = 'Have an account?'
    _username_input = '//input[@placeholder="Username"]'
    _email_input = '//input[@placeholder="Email"]'
    _password_input = '//input[@placeholder="Password"]'
    _signup_button = 'button'

    _settings_link = '//a[@routerlink="/settings"]'
    _error_message_item = '//app-list-errors//li'

    def goto_signup_page(self):
        self.elementClick(self._signup_link,'xpath')

    def reload_signup_page(self):
        self.getUrl(uc.SIGNUP_URL)

    def goto_login_page(self):
        self.elementClick(self._login_link,'xpath')

    def goto_home_page(self):
        self.elementClick(self._home_link, 'xpath')

    def click_have_account_link(self):
        self.elementClick(self._have_account_link,'link')

    def set_username(self, username):
        self.elementSendKeys(username , self._username_input,'xpath')

    def set_email(self, email):
        self.elementSendKeys(email , self._email_input,'xpath')

    def set_password(self, password):
        self.elementSendKeys(password , self._password_input,'xpath')

    def click_signup(self):
        # because ng_touched is set only after we leave the password field, the clicking of the signup button fails
        # to have the form in the right state, we will focus on email input field and then click the Sign up button
        # TODO investigate further
        self.elementClick(self._email_input, 'xpath')
        self.elementClick(self._signup_button, 'tag')

    def signup_user(self, username, email, password):
        self.set_username(username)
        self.set_email(email)
        self.set_password(password)

        self.click_signup()

    def is_signup_successful(self):
        element = self.waitForElement(self._settings_link, 'xpath')
        if element is not None:
            return True
        return False

    def get_error_list(self):
        elements = self.getElementList(self._error_message_item, 'xpath')
        actual_errors = []
        for element in elements:
            actual_errors.append(self.getText(element))
        return actual_errors

    def is_list_of_error_messages_correctly_displayed(self, expected_errors):
        return Util().verifyListsMatch(self.get_error_list(), expected_errors)