from main import MARSHMALLOW as marshmallow
from .stock import Stock


class StockSchema(marshmallow.ModelSchema):

    class Meta:
        model = Stock
