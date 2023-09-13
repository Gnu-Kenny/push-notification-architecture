from typing import Optional

from sqlalchemy.orm import Session

from producer.common.model.Curriculum import Curriculum
from producer.common.model.User import User
from producer.common.push.PushNotification import PushNotification
from producer.common.push.PushPolicyType import PushPolicyType
from producer.common.type.CommonResultCode import CommonResultCode
from producer.common.type.CustomException import CustomException
from producer.common.type.constants import ADMIN
from producer.common.util.util import transactional
from producer.lambda_example.model.CurriculumInfo import CurriculumInfo
from producer.lambda_example.model.CurriculumReponse import CurriculumResponse


@transactional
def post_curriculum(db: Session, curriculum_info: CurriculumInfo) -> CurriculumResponse:
    """
    :param db: DB 커넥션 객체
    :param curriculum_info: Request Body DTO
    :return : Response DTO
    """
    user: User = _get_user(db, user_id=curriculum_info.user_id)

    _verify_teacher_or_admin(user)

    curriculum: Curriculum = _create_curriculum(db=db, curriculum_info=curriculum_info)

    response: CurriculumResponse = _make_response(curriculum)
    return response


def make_push_notification(result: CurriculumResponse) -> PushNotification:
    push_notification = PushNotification(
        user_id=result.user_id,
        domain_type="curriculum",
        domain_id=result.curriculum_id,
        push_policy=PushPolicyType.TEACHER_CURRICULUM.name,
        msg_data=result.__dict__
    )

    return push_notification


def _get_user(db: Session, user_id: int) -> User:
    """
    유저 정보 조회
    """
    item: Optional[User] = db.get(User, user_id)

    if not item:
        raise CustomException(
            CommonResultCode.RESOURCE_NOT_FOUND,
            msg=f"존재하지 않는 유저입니다. user_id: {user_id}"
        )

    return item


def _verify_teacher_or_admin(user: User):
    """
    권한 유무 검증
    """
    if user.grade > ADMIN:
        raise CustomException(CommonResultCode.PERMISSION_DENIED, msg="해당 유저에게 작성 권한이 없습니다.")


def _create_curriculum(db: Session, curriculum_info: CurriculumInfo) -> Curriculum:
    curriculum: Curriculum = Curriculum(
        user_id=curriculum_info.user_id,
        title=curriculum_info.title,
        content=curriculum_info.content
    )

    db.add(curriculum)
    db.flush()

    return curriculum


def _make_response(curriculum: Curriculum) -> CurriculumResponse:
    """
    Response DTO 객체 생성
    """
    return CurriculumResponse(
        curriculum_id=curriculum.id,
        title=curriculum.title,
        content=curriculum.content,
        user_id=curriculum.user_id,
        created_at=curriculum.created_at
    )
