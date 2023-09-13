from producer.common.push.PushNotification import PushNotification
from producer.common.push.push_notification_service import apply_push_and_notification
from producer.common.util.util import api_handler
from producer.lambda_example.model.CurriculumInfo import CurriculumInfo
from producer.lambda_example.model.CurriculumReponse import CurriculumResponse
from producer.lambda_example.service import post_curriculum, make_push_notification


@api_handler
def lambda_handler(event, context):
    """
    온라인 강의 생성 API
    """
    # request body
    video_post_info: CurriculumInfo = CurriculumInfo.validate_input_and_extract(event)

    # service
    result: CurriculumResponse = post_curriculum(
        video_post_info=video_post_info
    )
    response = result.__dict__

    # 푸시/알림 요청
    push_noti: PushNotification = make_push_notification(result)
    apply_push_and_notification(push_noti)
    return response
