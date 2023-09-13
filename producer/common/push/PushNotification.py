class PushNotification:
    """
    user_id : 푸시를 요청하는 유저의 ID
    domain_type : 도메인 종류 (강의, 게시글 등)
    domain_id  : 도메인 ID
    push_policy : 푸시 정책
    msg_data : 푸시 메세지를 만들기 위한 데이터
    """

    def __init__(self,
                 user_id: int,
                 domain_type: str,
                 domain_id: id,
                 push_policy: str,
                 msg_data=dict,
                 **kwargs
                 ):
        self.user_id = user_id
        self.domain_type = domain_type
        self.domain_id = domain_id
        self.push_policy = push_policy
        self.sub_data = msg_data if msg_data else {}
