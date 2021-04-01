from sqlalchemy import Column, BigInteger, String, Sequence, Integer

from utils.db_api.db_gino import TimedBaseModel


class Item(TimedBaseModel):
    __tablename__ = 'items'
    id = Column(BigInteger, Sequence("item_id_sequence"), primary_key=True)
    label = Column(String(50))
    thumb_url = Column(String(200))
    description = Column(String(250))
    price = Column(Integer())
