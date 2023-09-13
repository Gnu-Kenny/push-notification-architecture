import json

from producer.common.type.CommonResultCode import CommonResultCode
from producer.common.type.CustomException import CustomException


class CurriculumInfo:

    def __init__(self, user_id, title, content):
        self.user_id = user_id if user_id else ""
        self.title = title if title else ""
        self.content = content if content else content

    @staticmethod
    def validate_input_and_extract(event: dict):
        """
        인자의 유효성을 판단하고 DTO로 변환하는 메서드
        :param event: AWS 인자
        :return CurriculumInfo: RequestBody DTO 객체
        """

        # body 존재 여부 확인 및 json 역직렬화
        request_body = event.get("body")
        if not request_body:
            raise CustomException(CommonResultCode.INVALID_BODY_CONTENTS, msg="Request Body가 존재하지 않습니다.")
        body = json.loads(request_body)

        # Request Body 객체 생성
        curriculum_info = CurriculumInfo(
            user_id=body.get("user_id", ""),
            title=body.get("title", ""),
            content=body.get("content", "")
        )

        # 프로퍼티 별 유효성 확인
        if not curriculum_info.user_id:
            raise CustomException(
                CommonResultCode.INVALID_BODY_CONTENTS,
                msg=f"유효하지 않은 값입니다. user_id: {curriculum_info.user_id}"
            )
        if not curriculum_info.title:
            raise CustomException(
                CommonResultCode.INVALID_BODY_CONTENTS,
                msg=f"유효하지 않은 값입니다. title: {curriculum_info.title}"
            )

        return curriculum_info
