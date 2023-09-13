from enum import Enum


class PushPolicyType(Enum):
    def __init__(self, code):
        self.code = code

    # POST/LECTURE/MAIN
    TEACHER_CURRICULUM = "TEACHER_CURRICULUM"

    # ERROR HANDLING
    UNKNOWN = ""

    @staticmethod
    def get_type(code: str):
        return type_map.get(code, PushPolicyType.UNKNOWN)

    def equals(self, code: str):
        return PushPolicyType[self.name] == self.get_type(code)


type_map = {}
for type_instance in PushPolicyType:
    type_map[type_instance.code] = type_instance
