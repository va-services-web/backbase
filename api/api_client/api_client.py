import requests
import utilities.custom_logger as cl
from utilities.util import Util
from traceback import print_stack
import jsonschema
from api import api_config as ep
import json
import os.path as path

class ApiClient(requests.Session):
    log = cl.customLogger()

    def __init__(self, api_name):
        super(ApiClient, self).__init__()
        self.hooks['response'].append(self.log_details)
        self.url = ''
        self.headers = {'Authorization': 'Basic {}'.format(ep.TOKEN),
                        'Content-Type': ep.CONTENT_TYPE
                        }
        # self.headers = {
        #     'Authorization': "Basic Y2FuZGlkYXRleDpxYS1pcy1jb29s",
        #     'User-Agent': "PostmanRuntime/7.17.1",
        #     'Accept': "*/*",
        #     'Cache-Control': "no-cache",
        #     'Host': "qa-task.backbasecloud.com",
        #     'Accept-Encoding': "gzip, deflate",
        #     'Connection': "keep-alive",
        #     'cache-control': "no-cache"
        # }
        self.util = Util()

    def log_details(self, response, *args, **kwargs):
        self.log.info("Request {}: {}".format(response.request.method, response.request.url))
        self.log.info("Request Headers: {}".format(response.request.headers))
        if response.request.body is not None:
            self.log.info("Request Body: {}".format(response.request.body))

        self.log.info("Response Status: {}, elapsed: {}s".format(response.status_code, response.elapsed.total_seconds()))
        self.log.info("Response Headers: {}".format(response.headers))
        if response.text != "":
            self.log.info("Response Body: {}".format(response.text))

    def read_all(self):
        self.log.info("READ ALL request")
        return self.get(self.url, headers=self.headers)

    def read(self, _id):
        self.log.info("READ request")
        return self.get(self.url + '/' + str(_id), headers=self.headers)

    def create(self, _new_data):
        self.log.info("CREATE request")
        return self.post(self.url, json=_new_data, headers=self.headers)

    def update(self, _id, _updated_data):
        self.log.info("UPDATE request")
        return self.put(self.url + '/' + str(_id), _updated_data, headers=self.headers)

    def remove(self, _id):
        self.log.info("DELETE request")
        return self.delete(self.url + '/' + str(_id), headers=self.headers)

    def verifyStatusCode(self, actualStatusCode, expectedStatusCode):
        try:
            return self.util.verifyNumbersMatch(actualStatusCode, expectedStatusCode)
        except:
            self.log.error("Failed to get status code")
            print_stack()
            return False

    def verifyErrorMessages(self, actualErrorMessage, expectedErrorMessage):
        try:
            return self.util.verifyDictionariesMatch(actualErrorMessage, expectedErrorMessage)
        except:
            self.log.error("Failed to get error message")
            print_stack()
            return False

    def validateJsonResponseVsSchema(self, jsonResponce, schema_filename):
        try:
            schemas_folder = path.normpath(path.join(path.dirname(path.abspath(__file__)), '..', 'schemas'))
            full_path = path.normpath(path.join(schemas_folder, schema_filename))
            with open(full_path, 'r') as f:
                schema_data = f.read()
            schema = json.loads(schema_data)

            v = jsonschema.Draft3Validator(schema)
            if len(sorted(v.iter_errors(jsonResponce), key=str)) == 0:
                return True
            else:
                self.log.error("Failed schema validation")
                for error in sorted(v.iter_errors(jsonResponce), key=str):
                    self.log.error(error.message)
                return False
        except jsonschema.ValidationError as e:
            self.log.error("Failed schema validation")
            self.log.error(e.message)
            return False
