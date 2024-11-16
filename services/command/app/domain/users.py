import uuid
from app.core.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import UUID, text


class Users(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    email: Mapped[str]
    hashed_password: Mapped[str]
    is_active: Mapped[bool]
    is_superuser: Mapped[bool]
    
