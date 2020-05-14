from flask_rest_jsonapi import ResourceDetail, ResourceList

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

from app import db

from app.models.plant import Plant, PlantVariety


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
    latin_name = fields.String(required=True)

    lifespan = fields.Nested('LifespanSchema')
    soil = fields.Nested('SoilSchema')
    plant_variety = fields.Nested('PlantVarietySchema', exclude=('plant',), many=True)

    lifespan_rel = Relationship(
        schema='LifespanSchema',
        type_='lifespan'
    )

    soil_rel = Relationship(
        schema='SoilSchema',
        type_='soil'
    )


class PlantVarietySchema(Schema):
    class Meta:
        type_ = 'variety'
        self_view = 'variety_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'variety_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    label = fields.String()

    plant = fields.Nested('PlantSchema', exclude=('plant_variety',))
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


class PlantList(ResourceList):
    schema = PlantSchema
    data_layer = {'session': db.session,
                  'model': Plant}


class PlantDetail(ResourceDetail):
    # make sure that all child varieties are deleted as well.
    def before_delete(self, args, kwargs):
        # delete all notes
        query = db.session.query(PlantVariety)
        query = query.filter(PlantVariety.plant_fk == kwargs['id'])
        query.delete()

    schema = PlantSchema
    data_layer = {'session': db.session,
                  'model': Plant}


class PlantVarietyList(ResourceList):
    schema = PlantVarietySchema
    data_layer = {'session': db.session,
                  'model': PlantVariety}


class PlantVarietyDetail(ResourceDetail):
    schema = PlantVarietySchema
    data_layer = {'session': db.session,
                  'model': PlantVariety}
