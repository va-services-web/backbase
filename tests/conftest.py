import pytest
from ui.base.webdriverfactory import WebDriverFactory
from ui.pages.authentication.authentication_page import AuthenticationPage
import ui.factories.signup_factory as SF
import ui.factories.error_factory as EF
from utilities.util import Util


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request):
    print("Running one time setUp")
    wdf = WebDriverFactory()
    driver = wdf.getWebDriverInstance()
    lp = AuthenticationPage()
    lp.authenticate()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()
    print('Runnning one time teardown')



@pytest.fixture()
def login_valid(request):
    return {
        "user": {
            "email": request.config.cache.get('email', None),
            "password": request.config.cache.get('password', None)
        }
    }

def signup_valid(userType):
    return SF.SignupSerializer().serialize(SF.Signup(), userType)

def signup_username_that_is_empty(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setUsername(''), userType), EF.ErrorSerializer().serialize({"username": "can't be blank"}, errorType)

def signup_username_that_contains_space(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setUsername(' '), userType), EF.ErrorSerializer().serialize({"username": "is invalid"}, errorType)

def signup_username_that_contains_underscore(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setUsername('_'), userType), EF.ErrorSerializer().serialize({"username": "is invalid"}, errorType)

def signup_username_that_contains_minus(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setUsername('-'), userType), EF.ErrorSerializer().serialize({"username": "is invalid"}, errorType)

def signup_username_that_contains_dot(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setUsername('.'), userType), EF.ErrorSerializer().serialize({"username": "is invalid"}, errorType)
# etc ...

# PASSWORD negative cases
def signup_password_that_is_empty(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setPassword(''), userType), EF.ErrorSerializer().serialize({"password": "can't be blank"}, errorType)

def signup_password_that_contains_space(userType):
    return SF.SignupSerializer().serialize(SF.Signup().setPassword(' '), userType)

def signup_password_that_contains_underscore(userType):
    return SF.SignupSerializer().serialize(SF.Signup().setPassword('_'), userType)

def signup_password_that_contains_minus(userType):
    return SF.SignupSerializer().serialize(SF.Signup().setPassword('-'), userType)

def signup_password_that_contains_dot(userType):
    return SF.SignupSerializer().serialize(SF.Signup().setPassword('.'), userType)
# etc ...

# EMAIL negative cases
def signup_email_that_is_empty(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setEmail(''), userType), EF.ErrorSerializer().serialize({"email": "can't be blank"}, errorType)

def signup_email_that_contains_space(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setEmail(' '), userType), EF.ErrorSerializer().serialize({"email": "is invalid"}, errorType)

def signup_email_that_contains_noAt(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setEmail(Util().randomEmail_noAt()), userType), EF.ErrorSerializer().serialize({"email": "is invalid"}, errorType)

def signup_email_that_contains_noDot(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setEmail(Util().randomEmail_noDot()), userType), EF.ErrorSerializer().serialize({"email": "is invalid"}, errorType)

def signup_email_that_contains_noAt_noDot(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setEmail(Util().randomEmail_noAt_noDot()), userType), EF.ErrorSerializer().serialize({"email": "is invalid"}, errorType)

# combinations
def signup_invalid_username_and_email(userType, errorType):
    return SF.SignupSerializer().serialize(SF.Signup().setUsername('v.a').setEmail('v.a@v'), userType), EF.ErrorSerializer().serialize({"username": "is invalid", "email": "is invalid"}, errorType)

