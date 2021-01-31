from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema, Relationship

from app import db
from app.models.plant.plant_child import PlantChild


class PlantChildSchema(Schema):
    class Meta:
        type_ = 'plant'
        self_view = 'plant_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plant_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    common_name = fields.String(required=True)

    lifespan = fields.Nested('LifespanSchema')
    soil = fields.Nested('SoilSchema')

    plant_rel = Relationship(
        schema='PlantSchema',
        type_='plant'
    )

    lifespan_rel = Relationship(
        schema='LifespanSchema',
        type_='lifespan'
    )

    soil_rel = Relationship(
        schema='SoilSchema',
        type_='soil'
    )


class PlantChildList(ResourceList):
    schema = PlantChildSchema
    data_layer = {'session': db.session,
                  'model': PlantChild}


class PlantChildDetail(ResourceDetail):
    schema = PlantChildSchema
    data_layer = {'session': db.session,
                  'model': PlantChild}
