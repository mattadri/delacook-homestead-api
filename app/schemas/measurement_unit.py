from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from app import db
from app.models.plant.measurement_unit import MeasurementUnit


class MeasurementUnitSchema(Schema):
    class Meta:
        type_ = 'measurement_unit'
        self_view = 'measurement_unit_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'measurement_unit_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label_singular = fields.String(required=True)
    label_plural = fields.String(required=True)


class MeasurementUnitList(ResourceList):
    schema = MeasurementUnitSchema
    data_layer = {'session': db.session,
                  'model': MeasurementUnit}


class MeasurementUnitDetail(ResourceDetail):
    schema = MeasurementUnitSchema
    data_layer = {'session': db.session,
                  'model': MeasurementUnit}
