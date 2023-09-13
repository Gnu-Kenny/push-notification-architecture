from datetime import datetime


class CurriculumResponse:
    def __init__(
            self,
            curriculum_id=0,
            title="",
            content="",
            user_id=0,
            created_at=datetime.now()
    ):
        self.curriculum_id = curriculum_id if curriculum_id else 0
        self.title = title if title else ""
        self.content = content if content else ""
        self.user_id = user_id if user_id else 0
        self.created_at = created_at if created_at else datetime.now()
