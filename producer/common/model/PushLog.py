from datetime import datetime

from sqlalchemy import *

from producer.common.model.database import Base


class PushLog(Base):
    __tablename__ = "push_log"

    id = Column(Integer, primary_key=True)
    reference_type = Column(String, doc="curriculum(강의), post(게시글)")
    reference_id = Column(Integer, doc="강의 또는 게시글의 id")
    push_policy = Column(String, default="")
    result = Column(Enum("SUCCESS", "FAIL", ""), default="", doc="성공 여부")
    status = Column(Enum("READY", "RUN", "DONE"), default="READY", doc="진행 상태: 준비/진행중/완료")
    description = Column(Text, default="")
    err_msg = Column(Text, default="")
    created_by = Column(Enum("PRODUCER", "CONSUMER"), nullable=False, doc="출처: 생상자/소비자")
    created_at = Column(DateTime, nullable=False, default=datetime.now())
