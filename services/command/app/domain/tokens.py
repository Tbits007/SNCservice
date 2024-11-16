import uuid
from app.core.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import UUID, ForeignKey, text
import datetime


class Tokens(Base):
    __tablename__ = "tokens"
    
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'))
    token: Mapped[str]
    expires_at: Mapped[datetime.datetime]
