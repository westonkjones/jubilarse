from sqlalchemy import Column, Sequence
from sqlalchemy.dialects import postgresql
from main import DATABASE as db

STOCKS_ID_SEQUENCE = Sequence('jobs_id_sequence')


class Stock(db.model):
    __tablename__ = 'stocks'
    id = Column(postgresql.BIGINT, STOCKS_ID_SEQUENCE, primary_key=True, server_default=STOCKS_ID_SEQUENCE.next_value())
    name = Column(postgresql.VARCHAR, nullable=False)
    symbol = Column(postgresql.VARCHAR, nullable=False)
    shares = Column(postgresql.INTEGER, nullable=False)
    bought = Column(postgresql.FLOAT, nullable=False)
    bought_date = Column(postgresql.TIMESTAMP(timezone=False), nullable=False)
    sold = Column(postgresql.FLOAT, nullable=False)
    sold_date = Column(postgresql.TIMESTAMP(timezone=False))

    def __init__(self, name: str, symbol: str, shares: int, bought: float, bought_date):
        self.name = name
        self.symbol = symbol
        self.shares = shares
        self.bought = bought
        self.bought_date = bought_date
