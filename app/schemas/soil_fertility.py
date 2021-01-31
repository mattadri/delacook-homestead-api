from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from app import db
from app.models.plant.soil_fertility import SoilFertility


class SoilFertilitySchema(Schema):
    class Meta:
        type_ = 'soil_fertility'
        self_view = 'soil_fertility_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'soil_fertility_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)


class SoilFertilityList(ResourceList):
    schema = SoilFertilitySchema
    data_layer = {'session': db.session,
                  'model': SoilFertility}


class SoilFertilityDetail(ResourceDetail):
    schema = SoilFertilitySchema
    data_layer = {'session': db.session,
                  'model': SoilFertility}
