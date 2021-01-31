from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema, Relationship

from app import db

from app.models.plant.genus import Genus


class GenusSchema(Schema):
    class Meta:
        type_ = 'genus'
        self_view = 'genus_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'genus_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)
    description = fields.String(required=False)

    family = fields.Nested('FamilySchema')

    family_rel = Relationship(
        schema='FamilySchema',
        type_='family'
    )


class GenusList(ResourceList):
    schema = GenusSchema
    data_layer = {'session': db.session,
                  'model': Genus}


class GenusDetail(ResourceDetail):
    schema = GenusSchema
    data_layer = {'session': db.session,
                  'model': Genus}
