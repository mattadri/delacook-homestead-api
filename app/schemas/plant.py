from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema, Relationship

from app import db
from app.models.plant.plant import Plant


class PlantSchema(Schema):
    class Meta:
        type_ = 'plant'
        self_view = 'plant_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plant_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    common_name = fields.String(required=True)
    description = fields.String()
    sub_species = fields.String()
    image_uri = fields.String()

    frost_tolerant = fields.Boolean()
    drought_tolerant = fields.Boolean()

    soil_ph_high = fields.Integer()
    soil_ph_low = fields.Integer()

    width = fields.Integer()
    height = fields.Integer()


class PlantList(ResourceList):
    schema = PlantSchema
    data_layer = {'session': db.session,
                  'model': Plant}


class PlantDetail(ResourceDetail):
    schema = PlantSchema
    data_layer = {'session': db.session,
                  'model': Plant}
