from utilities.util import Util


class Signup:
    def __init__(self):
        self.username = Util().randomUsername()
        self.password = Util().randomPassword()
        self.email = Util().randomEmail()

    def setUsername(self, username):
        self.username = username
        return self

    def setPassword(self, password):
        self.password = password
        return self

    def setEmail(self, email):
        self.email = email
        return self

class SignupSerializer:
    def serialize(self, signup, format):
        serializer = get_serializer(format)
        return serializer(signup)


def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'OBJ':
        return _serialize_to_obj
    else:
        raise ValueError(format)


def _serialize_to_json(signup):
    data = {
        'user': {
            'username': signup.username,
            'password': signup.password,
            'email': signup.email
        }
    }
    return data

def _serialize_to_obj(signup):
    return signup