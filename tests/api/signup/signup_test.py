from api.api_endpoints.signup.signup import Signup
from utilities.teststatus import TestStatus
import utilities.constants.status_codes as StatusCode

from tests.conftest import *


class TestSignup():

    @pytest.fixture(autouse = True)
    def classSetup(self):
        self.api = Signup()
        self.ts = TestStatus()

    # Create signup
    valid_signup = [
        signup_valid('JSON'),
    ]
    @pytest.mark.parametrize("user", valid_signup)
    def test_signup_new_user(self, request, user):
        response = self.api.signupUser(user)
        self.storeValidSignupDetails(request, user)

        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.OK)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.validateResponseVsSchema(response.json())
        self.ts.markFinal(request.node.name, result2, "Schema is valid")

    valid_signup_data = [
        signup_password_that_contains_space('JSON'),
        signup_password_that_contains_underscore('JSON'),
        signup_password_that_contains_minus('JSON'),
        signup_password_that_contains_dot('JSON'),
    ]
    @pytest.mark.parametrize("user", valid_signup_data)
    def test_signup_new_users(self, request, user):
        response = self.api.signupUser(user)

        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.OK)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.validateResponseVsSchema(response.json())
        self.ts.markFinal(request.node.name, result2, "Schema is valid")
    # Create duplicate signup (user & email)
    # Edit signup (user & password & email)

    # Signup - negatives
    invalid_signup_data = [
            signup_username_that_is_empty('JSON', 'JSON'),
            signup_username_that_contains_space('JSON', 'JSON'),
            signup_username_that_contains_underscore('JSON', 'JSON'),
            signup_username_that_contains_minus('JSON', 'JSON'),
            signup_username_that_contains_dot('JSON', 'JSON'),

            signup_password_that_is_empty('JSON', 'JSON'),

            signup_email_that_is_empty('JSON', 'JSON'),
            signup_email_that_contains_space('JSON', 'JSON'),
            signup_email_that_contains_noAt('JSON', 'JSON'),
            signup_email_that_contains_noDot('JSON', 'JSON'),
            signup_email_that_contains_noAt_noDot('JSON', 'JSON'),
            signup_invalid_username_and_email('JSON', 'JSON')
        ]
    @pytest.mark.parametrize("user,error", invalid_signup_data)
    def test_signup_invalid_signup_data(self, request, user, error):
        response = self.api.signupUser(user)

        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.UNPROCESSABLE_ENTITY)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.verifyErrorMessages(response.json(), error)
        self.ts.markFinal(request.node.name, result2, "Error message is correct")

    def storeValidSignupDetails(self, request, user):
        request.config.cache.set('username', user["user"]["username"])
        request.config.cache.set('email', user["user"]["email"])
        request.config.cache.set('password', user["user"]["password"])