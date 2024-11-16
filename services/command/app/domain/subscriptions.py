import uuid
from app.core.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import UUID, ForeignKey, text
import datetime


class Subscriptions(Base):
    __tablename__ = "subscriptions"
    
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'))
    subscription_type: Mapped[uuid.UUID] = mapped_column(ForeignKey("subscription_types.id", ondelete='CASCADE'))
    start_date: Mapped[datetime.datetime]
    end_date: Mapped[datetime.datetime]
