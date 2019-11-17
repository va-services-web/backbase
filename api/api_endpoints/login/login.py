from api.api_client.api_client import ApiClient
import utilities.custom_logger as cl
from api import api_config as ac


class Login(ApiClient):
    log = cl.customLogger()

    def __init__(self):
        super(Login, self).__init__(self.__class__.__name__)
        self.url = ac.ROOT_ENDPOINT + ac.LOGIN_ENDPOINT
        self.schema_file = ac.SIGNUP_USER_SCHEMA

    def loginUser(self, user):
        return self.create(user)

    def validateResponseVsSchema(self, jsonResponse):
        return self.validateJsonResponseVsSchema(jsonResponse, self.schema_file)