from datetime import datetime

from sqlalchemy import *

from producer.common.model.database import Base
from producer.common.type.constants import *


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, default="익명")
    email = Column(String)
    password = Column(String)
    delete_yn = Column(Enum(YES, NO), default=NO)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
