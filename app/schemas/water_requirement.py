from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from app import db
from app.models.plant.water_requirement import WaterRequirement


class WaterRequirementSchema(Schema):
    class Meta:
        type_ = 'water_requirement'
        self_view = 'water_requirement_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'water_requirement_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)


class WaterRequirementList(ResourceList):
    schema = WaterRequirementSchema
    data_layer = {'session': db.session,
                  'model': WaterRequirement}


class WaterRequirementDetail(ResourceDetail):
    schema = WaterRequirementSchema
    data_layer = {'session': db.session,
                  'model': WaterRequirement}
