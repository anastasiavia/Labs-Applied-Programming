from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Address(Base):
  __tablename__ = "address"
  idaddress = Column(Integer, primary_key=True)
  street = Column(String(45), nullable=False)
  city = Column(String(45), nullable=False)
  house_number = Column(Integer, nullable=True)


class User(Base):
  __tablename__ = 'user'
  iduser = Column(Integer, primary_key=True)
  username = Column(String(45), nullable=False)
  firstname = Column(String(45), nullable=False)
  lastname = Column(String(45), nullable=False)
  email = Column(String(45), nullable=False)
  password = Column(String(45), nullable=False)
  phone = Column(String(45), nullable=False)
  address_id = Column(Integer, ForeignKey("address.idaddress"))

  addressUser = relationship(Address, backref='user', lazy="joined", foreign_keys=[address_id])


class Item(Base):
  __tablename__ = "item"
  iditem = Column(Integer, primary_key=True)
  name = Column(String(45), nullable=False)
  amount = Column(Integer, nullable=True)
  price = Column(Integer, nullable=True)
  photoUrls = Column(String(45), nullable=False)
  status = Column(String(45), nullable=False)
  category = Column(String(45), nullable=False)


class Order(Base):
  __tablename__ = "order"

  idorder = Column(Integer, primary_key=True)
  quantity = Column(Integer, nullable=True)
  orderDate = Column(DateTime, nullable=False)
  status = Column(String(45), nullable=False)
  payment_method = Column(String(45), nullable=False)
  user_id = Column(Integer, ForeignKey("user.iduser"))
  item_id = Column(Integer, ForeignKey("item.iditem"))

  item_order = relationship(Item, backref='order', lazy="joined", foreign_keys=[item_id])
  user_order = relationship(User, backref='order', lazy="joined", foreign_keys=[user_id])
