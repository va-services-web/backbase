import json


class ErrorSerializer:
    def serialize(self, errorsDict, format):
        serializer = get_serializer(format)
        return serializer(errorsDict)


def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'STR':
        return _serialize_to_list
    else:
        raise ValueError(format)


def _serialize_to_json(errorsDict):
    return {'errors': errorsDict}


def _serialize_to_list(errorsDict):
    list_of_errors = []
    for key, value in errorsDict.items():
        list_of_errors.append('{} {}'.format(key, value))
    return list_of_errors