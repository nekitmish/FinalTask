from sqlalchemy import Column, String, BigInteger, sql, LargeBinary, Integer

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    referral = Column(BigInteger)
    coins = Column(Integer)

    query: sql.Select
