from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from app import db
from app.models.plant.family import Family


class FamilySchema(Schema):
    class Meta:
        type_ = 'family'
        self_view = 'family_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'family_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)
    description = fields.String(required=False)


class FamilyList(ResourceList):
    schema = FamilySchema
    data_layer = {'session': db.session,
                  'model': Family}


class FamilyDetail(ResourceDetail):
    schema = FamilySchema
    data_layer = {'session': db.session,
                  'model': Family}
