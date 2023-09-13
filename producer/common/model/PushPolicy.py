from datetime import datetime

from sqlalchemy import *

from producer.common.model.database import Base


class PushPolicy(Base):
    __tablename__ = "push_policy"

    id = Column(Integer, primary_key=True)
    push_type = Column(String, nullable=False)
    msg_format = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
