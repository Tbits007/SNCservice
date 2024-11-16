import uuid
from app.core.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import UUID, Numeric, text


class SubscriptionTypes(Base):
    __tablename__ = "subscription_types"
    
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float] = mapped_column(Numeric)