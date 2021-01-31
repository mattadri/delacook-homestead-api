from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from app import db
from app.models.plant.light_requirement import LightRequirement


class LightRequirementSchema(Schema):
    class Meta:
        type_ = 'light_requirement'
        self_view = 'light_requirement_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'light_requirement_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)


class LightRequirementList(ResourceList):
    schema = LightRequirementSchema
    data_layer = {'session': db.session,
                  'model': LightRequirement}


class LightRequirementDetail(ResourceDetail):
    schema = LightRequirementSchema
    data_layer = {'session': db.session,
                  'model': LightRequirement}
