from datetime import date

from sqlalchemy.orm import Mapped, relationship

from app.database import Base, str_uniq, int_pk


class Product(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    description: Mapped[str_uniq]
    price: Mapped[float]
    quantity: Mapped[int]

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class Order(Base):
    id: Mapped[int_pk]
    created_at: Mapped[date]
    status: Mapped[str]

    def __str__(self):
        return f"order id: {self.id} status: {self.status}"

    def __repr__(self):
        return str(self)


class OrderItem(Base):
    id: Mapped[int_pk]
    product_id: Mapped[int] = relationship("product.id")
    order_id: Mapped[int] = relationship("order.id")
