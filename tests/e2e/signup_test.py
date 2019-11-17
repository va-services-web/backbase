from ui.pages.signup.signup_page import SignupPage
from utilities.teststatus import TestStatus
from tests.conftest import *


@pytest.mark.usefixtures("oneTimeSetUp")
class TestSignup():
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ts = TestStatus()
        self.sp = SignupPage(self.driver)
        self.sp.reload_signup_page()

    @pytest.mark.parametrize("user", [signup_valid('OBJ')])
    def test_signup_successful(self, request, user):
        self.sp.signup_user(user.username, user.email, user.password)

        result1 = self.sp.is_signup_successful()
        self.ts.markFinal(request.node.name, result1, "Successful Signup")

    invalid_signup_data = [
        signup_invalid_username_and_email('OBJ', 'STR'),
    ]
    @pytest.mark.parametrize("user,errorList", invalid_signup_data)
    def test_signup_invalid(self, request, user, errorList):
        self.sp.signup_user(user.username, user.email, user.password)

        result1 = self.sp.is_list_of_error_messages_correctly_displayed(errorList)
        self.ts.markFinal(request.node.name, result1, "Invalid Signup")