from datetime import datetime

from sqlalchemy import *
from sqlalchemy.orm import relationship

from producer.common.model.database import Base
from producer.common.type.constants import *


class Curriculum(Base):
    __tablename__ = "curriculum"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), doc="작성자")
    title = Column(String)
    content = Column(Text)
    delete_yn = Column(Enum(YES, NO), default=NO)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

    user = relationship("User", foreign_keys=[user_id], backref="curriculum")

    def __init__(
            self,
            id=None,
            user_id=None,
            title=None,
            content=None,
            delete_yn=None,
            created_at=None
    ):
        self.id = id
        self.user_id = user_id if user_id else 0
        self.title = title if title else ""
        self.content = content if content else ""
        self.delete_yn = delete_yn if delete_yn else NO
        self.created_at = created_at if created_at else datetime.now()
