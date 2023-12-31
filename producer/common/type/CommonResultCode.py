from enum import Enum
from http import HTTPStatus

from producer.common.type.ResultCode import ResultCode


class CommonResultCode(ResultCode, Enum):
    SUCCESS = (HTTPStatus.OK, "SUCCESS", "success")
    EXTERNAL_NETWORK_ERROR = (HTTPStatus.OK, "EXTERNAL_NETWORK_ERROR", "external_network_err")

    BAD_REQUEST = (HTTPStatus.BAD_REQUEST, "BAD_REQUEST", "input is wrong")
    PERMISSION_DENIED = (HTTPStatus.BAD_REQUEST, "PERMISSION_DENIED", "request is denied by permission")
    UNEXPECTED_QUERY_PARAMETER = (HTTPStatus.BAD_REQUEST, "UNEXPECTED_QUERY_PARAMETER", "unexpected query parameter")
    INVALID_PARAMETER = (HTTPStatus.BAD_REQUEST, "INVALID_PARAMETER", "invalid parameter")
    INVALID_QUERY_PARAMETER = (HTTPStatus.BAD_REQUEST, "INVALID_QUERY_PARAMETER", "invalid query parameter")
    INVALID_PATH_PARAMETER = (HTTPStatus.BAD_REQUEST, "INVALID_PATH_PARAMETER", "invalid path parameter")
    INVALID_AUTH_PARAMETER = (HTTPStatus.BAD_REQUEST, "INVALID_AUTH_PARAMETER", "invalid auth parameter")
    INVALID_REQUEST_BODY = (HTTPStatus.BAD_REQUEST, "INVALID_REQUEST_BODY", "invalid requestBody")
    INVALID_BODY_CONTENTS = (HTTPStatus.BAD_REQUEST, "INVALID_BODY_CONTENTS", "invalid body contents")
    RESOURCE_NOT_FOUND = (HTTPStatus.BAD_REQUEST, "RESOURCE_NOT_FOUND", "can't find the resource")
    BUILD_RESPONSE_FAIL = (HTTPStatus.BAD_REQUEST, "BUILD_RESPONSE_FAIL", "BUILD_RESPONSE_FAIL")
    UNEXPECTED_ERROR = (HTTPStatus.BAD_REQUEST, "UNEXPECTED_ERROR", "UNEXPECTED_ERROR")
    EXTERNAL_CONNECTION_ERROR = (HTTPStatus.BAD_REQUEST, "EXTERNAL_CONNECTION_ERROR", "EXTERNAL_CONNECTION_ERROR")

    UNAUTHORIZED = (HTTPStatus.UNAUTHORIZED, "UNAUTHORIZED", "request unauthorized")
