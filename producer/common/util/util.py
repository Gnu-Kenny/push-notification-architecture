from botocore.args import logger

from producer.common.model.database import SessionLocal
from producer.common.util.custom_response_builder import build_success_response, build_fail_response


def api_handler(func):
    """
    사용자 정의 예외 처리 데코레이터
    """

    def wrapper(*args, **kwargs):
        event = args[0]
        context = args[1]

        try:
            response_data = func(event, context)
            response = build_success_response(response_data)

        except Exception as exc:
            logger.exception("dump parameter", exc, event, context)
            response = build_fail_response(exc)

        return response

    return wrapper


def transactional(func):
    def wrapper(*args, **kwargs):
        db = SessionLocal()
        try:
            result = func(db=db, *args, **kwargs)
            db.commit()

            return result

        except Exception as exc:
            db.rollback()
            raise exc
        finally:
            db.close()

    return wrapper
