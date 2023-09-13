import json


class Json:
    @classmethod
    def to_json(cls, string: str):
        return json.loads(string)

    @classmethod
    def stringify(cls, obj: object, **kwargs):
        try:
            return json.dumps(obj, cls=ClsJsonEncoder, ensure_ascii=False, **kwargs)
        except Exception as exception:
            raise exception

    @staticmethod
    def is_json(obj):
        try:
            if type(obj) is str:
                json_object = json.loads(obj)
                iter(json_object)
            else:
                return False

        except Exception as e:
            return False

        return True


class ClsJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, object):
                if hasattr(obj, "__dict__"):
                    return obj.__dict__
                else:
                    return str(obj)
            else:
                return json.JSONEncoder.default(self, obj)
        except Exception as exception:
            raise exception
