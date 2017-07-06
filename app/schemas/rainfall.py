from flask_rest_jsonapi import ResourceDetail, ResourceList

from app.models.rainfall import RainfallTotal

from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

from app import db


# RAINFALL TOTALS
class RainfallTotalSchema(Schema):
    class Meta:
        type_ = 'rainfalltotals'
        self_view = 'rainfall_total_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'rainfall_total_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    date = fields.Date()
    amount = fields.Float()


class RainfallTotalList(ResourceList):
    schema = RainfallTotalSchema
    data_layer = {'session': db.session,
                  'model': RainfallTotal}


class RainfallTotalDetail(ResourceDetail):
    schema = RainfallTotalSchema
    data_layer = {'session': db.session,
                  'model': RainfallTotal}
