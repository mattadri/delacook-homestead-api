from flask_rest_jsonapi import ResourceDetail, ResourceList

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

from app import db

from app.models.bed import Bed, BedPlant


class BedSchema(Schema):
    class Meta:
        type_ = 'bed'
        self_view = 'garden_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'garden_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)

    bed_plant = fields.Nested('BedPlantSchema', exclude=('bed',), many=True)


class BedList(ResourceList):
    schema = BedSchema
    data_layer = {'session': db.session,
                  'model': Bed}


class BedDetail(ResourceDetail):
    schema = BedSchema
    data_layer = {'session': db.session,
                  'model': Bed}


class BedPlantSchema(Schema):
    class Meta:
        type_ = 'bed_plant'
        self_view = 'bed_plant_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'bed_plant_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    bed = fields.Nested('BedSchema')
    plant = fields.Nested('PlantSchema')

    bed_rel = Relationship(
        schema='BedSchema',
        type_='bed',
        required=True
    )

    plant_rel = Relationship(
        schema='PlantSchema',
        type_='plant',
        required=True
    )


class BedPlantList(ResourceList):
    schema = BedPlantSchema
    data_layer = {'session': db.session,
                  'model': BedPlant}


class BedPlantDetail(ResourceDetail):
    schema = BedPlantSchema
    data_layer = {'session': db.session,
                  'model': BedPlant}
