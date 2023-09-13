from typing import Optional

from sqlalchemy import *
from sqlalchemy.orm import Session

from producer.common.model.PushLog import PushLog
from producer.common.model.ResultType import ResultType
from producer.common.model.StatusType import StatusType
from producer.common.push.PushNotification import PushNotification
from producer.common.util.slack_util import send_push_slack


def change_log(db: Session, log: PushLog, status: StatusType = None, description=None, err_msg=None,
               result: ResultType = None):
    """
    push 상태를 변경하고 저장하는 함수
    """
    if status is not None:
        log.status = status.code
    if description is not None:
        log.description = description
    if err_msg is not None:
        log.err_msg = err_msg
    if result is not None:
        log.result = result.code

    if result and result == result.FAIL:
        send_push_slack(log)

    db.commit()
    return log


def get_or_create_push_log(db: Session, push_notification: PushNotification, created_by: str):
    push_log: PushLog = PushLog(
        domain_type=push_notification.domain_type,
        domain_id=push_notification.domain_id,
        push_policy=push_notification.push_policy,
        created_by=created_by
    )

    prev_push_log: Optional[PushLog] = _find_log_by(db, push_log)
    if prev_push_log:
        prev_push_log.status = StatusType.READY.code
        prev_push_log.result = ResultType.UNKNOWN.code

        db.commit()
        return prev_push_log

    db.add(push_log)
    db.commit()

    return push_log


def _find_log_by(db: Session, push_log: PushLog) -> Optional[PushLog]:
    stmt = select(PushLog).where(
        and_(
            PushLog.reference_type == push_log.reference_type,
            PushLog.reference_id == push_log.reference_id,
            PushLog.push_policy == push_log.push_policy,
            PushLog.created_by == push_log.created_by,
        )
    )

    item = db.scalars(stmt).one()

    return item
