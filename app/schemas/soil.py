from flask_rest_jsonapi import ResourceDetail, ResourceList

from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

from app import db

from app.models.soil import Soil


class SoilSchema(Schema):
    class Meta:
        type_ = 'soil'
        self_view = 'soil_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'soil_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)


class SoilList(ResourceList):
    schema = SoilSchema
    data_layer = {'session': db.session,
                  'model': Soil}


class SoilDetail(ResourceDetail):
    schema = SoilSchema
    data_layer = {'session': db.session,
                  'model': Soil}
