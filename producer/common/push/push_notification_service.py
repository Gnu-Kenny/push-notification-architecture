import traceback

import boto3
from botocore.args import logger
from botocore.config import Config
from sqlalchemy.orm import Session

from producer.common.logger.push_log_service import get_or_create_push_log, change_log
from producer.common.model.ResultType import ResultType
from producer.common.model.StatusType import StatusType
from producer.common.push.PushNotification import PushNotification
from producer.common.type.constants import SQS_NOTI, SQS_PUSH, PRODUCER
from producer.common.util.Json import Json
from producer.common.util.sqs_util import send_single_message
from producer.common.util.util import transactional


@transactional
def apply_push_and_notification(db: Session, push_notification: PushNotification):
    # 로그 생성
    push_log = get_or_create_push_log(db=db, push_notification=push_notification, created_by=PRODUCER)
    try:
        change_log(db=db, log=push_log, status=StatusType.RUNNING)

        # sqs message body ( type : str )
        message_dict = push_notification.__dict__
        json_message = Json.stringify(message_dict)

        change_log(db=db, log=push_log, description=f"메세지 생성")

        sqs = boto3.resource("sqs", config=Config(tcp_keepalive=True))

        queue_noti = sqs.Queue(SQS_NOTI)
        queue_push = sqs.Queue(SQS_PUSH)

        send_single_message(queue_noti, json_message)
        send_single_message(queue_push, json_message)

        change_log(db=db, log=push_log, status=StatusType.TERMINATED, description="성공", result=ResultType.SUCCESS)

    except Exception as err:
        err_msg = traceback.format_exc()
        change_log(db=db, log=push_log, status=StatusType.TERMINATED, err_msg=err_msg, result=ResultType.FAIL)
        logger.info_status(
            f"error occurred in sending message to sqs for push and notification\n{err_msg}, {err.__str__()}")
