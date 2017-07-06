from flask import request

from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

from app import db

from app.models.plant import Plant, LifeSpan, LeafCycle, WoodType, Type


# PLANTS
class PlantSchema(Schema):
    class Meta:
        type_ = 'plants'
        self_view = 'plant_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plant_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    friendlyname = fields.String(attribute='friendly_name', required=True)
    latinname = fields.String(attribute='latin_name')
    droughttolerant = fields.Boolean(attribute='drought_tolerant')
    medicinal = fields.Boolean()
    edible = fields.Boolean()
    imagelarge = fields.String(attribute='image_large')
    imagesmall = fields.String(attribute='image_small')
    types = Relationship(
        attribute='type',
        self_view='plant_type',
        self_view_kwargs={'id': '<id>'},
        related_view='type_detail',
        related_view_kwargs={'id': '<id>'},
        schema='TypeSchema',
        type_='types')
    woodtypes = Relationship(
        attribute='wood_type',
        self_view='plant_type',
        self_view_kwargs={'id': '<id>'},
        related_view='woodtype_detail',
        related_view_kwargs={'id': '<id>'},
        many=False,
        schema='WoodTypeSchema',
        type_='woodtypes')
    lifespans = Relationship(
        attribute='lifespan',
        self_view='plant_type',
        self_view_kwargs={'id': '<id>'},
        related_view='lifespan_detail',
        related_view_kwargs={'id': '<id>'},
        many=False,
        schema='LifespanSchema',
        type_='lifespans')
    leafcycles = Relationship(
        attribute='leaf_cycle',
        self_view='plant_type',
        self_view_kwargs={'id': '<id>'},
        related_view='leafcycle_detail',
        related_view_kwargs={'id': '<id>'},
        many=False,
        schema='LeafCycleSchema',
        type_='leafcycles')


class LifespanSchema(Schema):
    class Meta:
        type_ = 'lifespans'
        self_view = 'lifespan_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'lifespan_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    enum = fields.String(required=True)
    name = fields.String(required=True)
    plants = Relationship(
        self_view='lifespan_plant',
        self_view_kwargs={'id': '<id>'},
        related_view='plant_detail',
        related_view_kwargs={'id': '<id>'},
        many=True,
        schema='PlantSchema',
        type_='plants'
    )


class TypeSchema(Schema):
    class Meta:
        type_ = 'types'
        self_view = 'type_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'type_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    enum = fields.String(required=True)
    name = fields.String(required=True)
    plants = Relationship(
        self_view='type_plant',
        self_view_kwargs={'id': '<id>'},
        related_view='plant_detail',
        related_view_kwargs={'id': '<id>'},
        many=True,
        schema='PlantSchema',
        type_='plants'
    )


class WoodTypeSchema(Schema):
    class Meta:
        type_ = 'woodtypes'
        self_view = 'woodtype_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'woodtype_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    enum = fields.String(required=True)
    name = fields.String(required=True)
    plants = Relationship(
            self_view='woodtype_plant',
            self_view_kwargs={'id': '<id>'},
            related_view='plant_detail',
            related_view_kwargs={'id': '<id>'},
            many=True,
            schema='PlantSchema',
            type_='plants'
        )


class LeafCycleSchema(Schema):
    class Meta:
        type_ = 'leafcycles'
        self_view = 'leafcycle_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'leafcycle_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    enum = fields.String(required=True)
    name = fields.String(required=True)
    plants = Relationship(
        self_view='leafcycle_plant',
        self_view_kwargs={'id': '<id>'},
        related_view='plant_detail',
        related_view_kwargs={'id': '<id>'},
        many=True,
        schema='PlantSchema',
        type_='plants'
    )


class PlantList(ResourceList):
    def before_create_object(self, data, view_kwargs):
        request_data = request.json

        if 'relationships' in request_data['data']:
            relationships = request_data['data']['relationships']

            if 'type' in relationships:
                data['type_fk'] = int(relationships['type']['data']['id'])

            if 'woodtype' in relationships:
                data['wood_type_fk'] = int(relationships['woodtype']['data']['id'])

            if 'leafcycle' in relationships:
                data['leaf_cycle_fk'] = int(relationships['leafcycle']['data']['id'])

            if 'lifespan' in relationships:
                data['lifespan_fk'] = int(relationships['lifespan']['data']['id'])

    schema = PlantSchema
    data_layer = {'session': db.session,
                  'model': Plant,
                  'methods': {
                      'before_create_object': before_create_object
                  }}


class PlantDetail(ResourceDetail):
    schema = PlantSchema
    data_layer = {'session': db.session,
                  'model': Plant}


class PlantRelationship(ResourceRelationship):
    schema = PlantSchema
    data_layer = {'session': db.session,
                  'model': Plant}


class LifeSpanList(ResourceList):
    schema = LifespanSchema
    data_layer = {'session': db.session,
                  'model': LifeSpan}


class LifeSpanDetail(ResourceDetail):
    schema = LifespanSchema
    data_layer = {'session': db.session,
                  'model': LifeSpan}


class LifeSpanRelationship(ResourceRelationship):
    schema = LifespanSchema
    data_layer = {'session': db.session,
                  'model': LifeSpan}


class TypeList(ResourceList):
    schema = TypeSchema
    data_layer = {'session': db.session,
                  'model': Type}


class TypeDetail(ResourceDetail):
    schema = TypeSchema
    data_layer = {'session': db.session,
                  'model': Type}


class TypeRelationship(ResourceRelationship):
    schema = TypeSchema
    data_layer = {'session': db.session,
                  'model': Type}


class WoodTypeList(ResourceList):
    schema = WoodTypeSchema
    data_layer = {'session': db.session,
                  'model': WoodType}


class WoodTypeDetail(ResourceDetail):
    schema = WoodTypeSchema
    data_layer = {'session': db.session,
                  'model': WoodType}


class WoodTypeRelationship(ResourceRelationship):
    schema = WoodTypeSchema
    data_layer = {'session': db.session,
                  'model': WoodType}


class LeafCycleList(ResourceList):
    schema = LeafCycleSchema
    data_layer = {'session': db.session,
                  'model': LeafCycle}


class LeafCycleDetail(ResourceDetail):
    schema = LeafCycleSchema
    data_layer = {'session': db.session,
                  'model': LeafCycle}


class LeafCycleRelationship(ResourceRelationship):
    schema = LeafCycleSchema
    data_layer = {'session': db.session,
                  'model': LeafCycle}
