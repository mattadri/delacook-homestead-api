from flask_rest_jsonapi import ResourceDetail, ResourceList

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

from app import db

from app.models.bed import Bed
from app.models.garden import Garden, GardenBed


class GardenSchema(Schema):
    class Meta:
        type_ = 'garden'
        self_view = 'garden_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'garden_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)

    garden_bed = fields.Nested('GardenBedSchema', exclude=('garden',), many=True)


class GardenList(ResourceList):
    schema = GardenSchema
    data_layer = {'session': db.session,
                  'model': Garden}


class GardenDetail(ResourceDetail):
    schema = GardenSchema
    data_layer = {'session': db.session,
                  'model': Garden}


class GardenBedSchema(Schema):
    class Meta:
        type_ = 'garden_bed'
        self_view = 'garden_bed_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'garden_bed_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    garden = fields.Nested('GardenSchema')
    bed = fields.Nested('BedSchema')

    garden_rel = Relationship(
        schema='GardenSchema',
        type_='garden',
        required=True
    )

    bed_rel = Relationship(
        schema='BedSchema',
        type_='bed',
        required=True
    )


class GardenBedList(ResourceList):
    schema = GardenBedSchema
    data_layer = {'session': db.session,
                  'model': GardenBed}


class GardenBedDetail(ResourceDetail):
    schema = GardenBedSchema
    data_layer = {'session': db.session,
                  'model': GardenBed}
