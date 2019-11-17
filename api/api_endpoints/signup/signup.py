from api.api_client.api_client import ApiClient
import utilities.custom_logger as cl
from api import api_config as ac


class Signup(ApiClient):
    log = cl.customLogger()

    def __init__(self):
        super(Signup, self).__init__(self.__class__.__name__)
        self.url = ac.ROOT_ENDPOINT + ac.SIGNUP_ENDPOINT
        self.schema_file = ac.SIGNUP_USER_SCHEMA

    def signupUser(self, new_user):
        return self.create(new_user)

    def validateResponseVsSchema(self, jsonResponse):
        return self.validateJsonResponseVsSchema(jsonResponse, self.schema_file)

