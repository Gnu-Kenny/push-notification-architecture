from datetime import datetime

from sqlalchemy import *

from producer.common.model.database import Base
from producer.common.type.constants import *


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    content = Column(Text)
    delete_yn = Column(Enum(YES, NO), default=NO)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
