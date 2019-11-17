import pytest
from api.api_endpoints.login.login import Login
from utilities.teststatus import TestStatus
import utilities.constants.status_codes as StatusCode


class TestLogin():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.api = Login()
        self.ts = TestStatus()

    # Login user - valid
    def test_login_user(self, request, login_valid):
        response = self.api.loginUser(login_valid)

        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.OK)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.validateResponseVsSchema(response.json())
        self.ts.markFinal(request.node.name, result2, "Schema is valid")

    # Login user - negatives