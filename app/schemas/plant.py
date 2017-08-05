from flask import request

from sqlalchemy.orm.exc import NoResultFound

from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from flask_rest_jsonapi.exceptions import ObjectNotFound

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

from app import db

from app.models.plant import Plant, LifeSpan, LeafCycle, WoodType, Type, PlantNote, PlantingPhysicalSource, \
    PlantLineage, PlantGeneration, PlantLineageGeneration, Planting, PlantingNotes, PlantGenerationSeedCollection, \
    PlantCloning, PlantCloningNotes, PlantHarvest, PlantHarvestNotes


# PLANTS
# SCHEMAS
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
        schema='WoodTypeSchema',
        type_='woodtypes')
    lifespans = Relationship(
        attribute='lifespan',
        self_view='plant_type',
        self_view_kwargs={'id': '<id>'},
        related_view='lifespan_detail',
        related_view_kwargs={'id': '<id>'},
        schema='LifespanSchema',
        type_='lifespans')
    leafcycles = Relationship(
        attribute='leaf_cycle',
        self_view='plant_type',
        self_view_kwargs={'id': '<id>'},
        related_view='leafcycle_detail',
        related_view_kwargs={'id': '<id>'},
        schema='LeafCycleSchema',
        type_='leafcycles')
    plantnotes = Relationship(
        self_view='plant_notes',
        self_view_kwargs={'id': '<id>'},
        related_view='plantnote_list',
        related_view_kwargs={'id': '<id>'},
        many=True,
        schema='PlantNoteSchema',
        type_='plantnotes')
    plantlineages = Relationship(
        self_view='plant_lineages',
        self_view_kwargs={'id': '<id>'},
        related_view='plantlineage_list',
        related_view_kwargs={'id': '<id>'},
        many=True,
        schema='PlantLineageSchema',
        type_='plantlineages')


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


class PlantNoteSchema(Schema):
    class Meta:
        type_ = 'plantnotes'
        self_view = 'plantnote_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plantnote_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    notedate = fields.Date(attribute='note_date')
    note = fields.String()
    plant = Relationship(
        attribute='plant',
        self_view='plantnote_plant',
        self_view_kwargs={'id': '<id>'},
        related_view='plant_detail',
        related_view_kwargs={'plant_note_id': '<id>'},
        schema='PlantSchema',
        type_='plants')


class PlantLineageSchema(Schema):
    class Meta:
        type_ = 'plantlineages'
        self_view = 'plantlineage_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plantlineage_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    isdead = fields.Boolean(attribute='is_dead')
    lineagesource = fields.String(attribute='lineage_source')
    datelineagestarted = fields.Date(attribute='date_lineage_started')
    plant = Relationship(
        attribute='plant',
        self_view='plantlineage_plant',
        self_view_kwargs={'id': '<id>'},
        related_view='plant_detail',
        related_view_kwargs={'plant_note_id': '<id>'},
        schema='PlantSchema',
        type_='plants')
    plantingphysicalsource = Relationship(
        attribute='planting_physical_source',
        self_view='plantlineage_plantingphysicalsource',
        self_view_kwargs={'id': '<id>'},
        related_view='plantingphysicalsource_detail',
        related_view_kwargs={'id': '<id>'},
        schema='PlantingPhysicalSourceSchema',
        type_='plantingphysicalsources')
    lineagegenerations = Relationship(
        self_view='plant_lineagegenerations',
        self_view_kwargs={'id': '<id>'},
        related_view='plantlineagegeneration_list',
        related_view_kwargs={'id': '<id>'},
        many=True,
        schema='PlantLineageGenerationSchema',
        type_='plantlineagegenerations')


class PlantingPhysicalSourceSchema(Schema):
    class Meta:
        type_ = 'plantingphysicalsources'
        self_view = 'plantingphysicalsource_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plantingphysicalsource_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    enum = fields.String(required=True)
    name = fields.String(required=True)


class PlantGenerationSchema(Schema):
    class Meta:
        type_ = 'plantgenerations'
        self_view = 'plantgeneration_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plantgeneration_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    plantings = Relationship(
        self_view='plantgeneration_plantings',
        self_view_kwargs={'id': '<id>'},
        related_view='planting_list',
        related_view_kwargs={'id': '<id>'},
        many=True,
        schema='PlantingSchema',
        type_='plantings')


class PlantGenerationSeedCollectionSchema(Schema):
    class Meta:
        type_ = 'plantgenerationseedcollections'
        self_view = 'plantgenerationseedcollection_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plantgenerationseedcollection_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    dateseedsharvested = fields.Date(attribute='date_seeds_harvested')
    totalseedsharvested = fields.Integer(attribute='total_seeds_harvested')
    dateseedspackaged = fields.Date(attribute='date_seeds_packaged')
    plantgeneration = Relationship(
        attribute='plant_generation',
        self_view='plantgenerationseedcollection_plantgeneration',
        self_view_kwargs={'id': '<id>'},
        related_view='plantgeneration_detail',
        related_view_kwargs={'id': '<id>'},
        schema='PlantGenerationSchema',
        type_='plantgenerations')


class PlantLineageGenerationSchema(Schema):
    class Meta:
        type_ = 'plantlineagegenerations'
        self_view = 'plantlineagegeneration_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plantlineagegeneration_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    generationslot = fields.Integer(attribute='generation_slot')
    isorigin = fields.Boolean(attribute='is_origin')
    plantlineage = Relationship(
        attribute='plant_lineage',
        self_view='plantlineagegeneration_plantlineage',
        self_view_kwargs={'id': '<id>'},
        related_view='plantlineage_detail',
        related_view_kwargs={'id': '<id>'},
        schema='PlantLineageSchema',
        type_='plantlineages')
    plantgeneration = Relationship(
        attribute='plant_generation',
        self_view='plantlineagegeneration_plantgeneration',
        self_view_kwargs={'id': '<id>'},
        related_view='plantgeneration_detail',
        related_view_kwargs={'id': '<id>'},
        schema='PlantGenerationSchema',
        type_='plantgenerations')


class PlantingSchema(Schema):
    class Meta:
        type_ = 'plantings'
        self_view = 'planting_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'planting_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    seedsstarted = fields.Integer(attribute='seeds_started')
    dateseedsstarted = fields.Date(attribute='date_seeds_started')
    startingmedium = fields.String(attribute='starting_medium')
    seedssprouted = fields.Integer(attribute='seeds_sprouted')
    datefirstseedssprouted = fields.Date(attribute='date_first_seeds_sprouted')
    sproutsplanted = fields.Integer(attribute='sprouts_planted')
    datesproutsplanted = fields.Date(attribute='date_sprouts_planted')
    plantssurvived = fields.Integer(attribute='plants_survived')
    datenextgenerationseedscollected = fields.Date(attribute='date_next_generation_seeds_collected')
    plantgeneration = Relationship(
        attribute='plant_generation',
        self_view='planting_plantgeneration',
        self_view_kwargs={'id': '<id>'},
        related_view='plantgeneration_detail',
        related_view_kwargs={'id': '<id>'},
        schema='PlantGenerationSchema',
        type_='plantgenerations')
    plantingphysicalsource = Relationship(
        attribute='planting_physical_source',
        self_view='planting_plantingphysicalsource',
        self_view_kwargs={'id': '<id>'},
        related_view='plantingphysicalsource_detail',
        related_view_kwargs={'id': '<id>'},
        schema='PlantingPhysicalSourceSchema',
        type_='plantingphysicalsources')


class PlantingNotesSchema(Schema):
    class Meta:
        type_ = 'plantingnotes'
        self_view = 'plantingnote_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plantingnote_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    notedate = fields.Date(attribute='note_date')
    note = fields.String()
    planting = Relationship(
        self_view='plantingnote_planting',
        self_view_kwargs={'id': '<id>'},
        related_view='planting_detail',
        related_view_kwargs={'id': '<id>'},
        schema='PlantingSchema',
        type_='plantings'
    )


class CloningSchema(Schema):
    class Meta:
        type_ = 'clonings'
        self_view = 'cloning_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'cloning_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    datecloned = fields.Date(attribute='date_cloned')
    numbercloned = fields.Integer(attribute='number_cloned')
    numberrooted = fields.Integer(attribute='number_rooted')
    datefirstplantrooted = fields.Date(attribute='date_first_plant_rooted')
    clonesplanted = fields.Integer(attribute='clones_planted')
    dateclonesplanted = fields.Date(attribute='date_clones_planted')
    clonessurvived = fields.Integer(attribute='clones_survived')
    datenextgenerationseedscollected = fields.Date(attribute='date_next_generation_seeds_collected')
    roothormoneused = fields.Boolean(attribute='root_hormone_used')
    roothormonetype = fields.String(attribute='root_hormone_type')
    rootingmedium = fields.String(attribute='rooting_medium')
    plantgeneration = Relationship(
        attribute='plant_generation',
        self_view='planting_plantgeneration',
        self_view_kwargs={'id': '<id>'},
        related_view='plantgeneration_detail',
        related_view_kwargs={'id': '<id>'},
        schema='PlantGenerationSchema',
        type_='plantgenerations')
    plantingphysicalsource = Relationship(
        attribute='planting_physical_source',
        self_view='cloning_plantingphysicalsource',
        self_view_kwargs={'id': '<id>'},
        related_view='plantingphysicalsource_detail',
        related_view_kwargs={'id': '<id>'},
        schema='PlantingPhysicalSourceSchema',
        type_='plantingphysicalsources')


class CloningNotesSchema(Schema):
    class Meta:
        type_ = 'cloningnotes'
        self_view = 'cloningnote_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'cloningnote_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    notedate = fields.Date(attribute='note_date')
    note = fields.String()
    plantcloning = Relationship(
        attribute='plant_cloning',
        self_view='cloningnote_cloning',
        self_view_kwargs={'id': '<id>'},
        related_view='cloning_detail',
        related_view_kwargs={'id': '<id>'},
        schema='CloningSchema',
        type_='clonings'
    )


class PlantHarvestSchema(Schema):
    class Meta:
        type_ = 'plantharvests'
        self_view = 'plantharvest_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plantharvest_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    startdate = fields.Date(attribute='start_date')
    finishdate = fields.Date(attribute='finish_date')
    gramsharvested = fields.Integer(attribute='grams_harvested')
    plantgeneration = Relationship(
        attribute='plant_generation',
        self_view='harvest_plantgeneration',
        self_view_kwargs={'id': '<id>'},
        related_view='plantgeneration_detail',
        related_view_kwargs={'id': '<id>'},
        schema='PlantGenerationSchema',
        type_='plantgenerations')


class PlantHarvestNoteSchema(Schema):
    class Meta:
        type_ = 'plantharvestnotes'
        self_view = 'plantharvestnote_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plantharvestnote_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    notedate = fields.Date(attribute='note_date')
    note = fields.String()
    plantharvest = Relationship(
        attribute='plant_harvest',
        self_view='harvestnote_harvest',
        self_view_kwargs={'id': '<id>'},
        related_view='plantharvest_detail',
        related_view_kwargs={'id': '<id>'},
        schema='PlantHarvestSchema',
        type_='plantharvests'
    )


# RESOURCES
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
    def before_get_object(self, view_kwargs):
        if view_kwargs.get('plant_note_id') is not None:
            try:
                plant_note = self.session.query(PlantNote).filter_by(
                    id=view_kwargs['plant_note_id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'plant_note_id'},
                                     "Plant Note: {} not found".format(
                                         view_kwargs['plant_note_id']))
            else:
                if plant_note.plant is not None:
                    view_kwargs['id'] = plant_note.plant.id
                else:
                    view_kwargs['id'] = None

    schema = PlantSchema
    data_layer = {'session': db.session,
                  'model': Plant,
                  'methods': {'before_get_object': before_get_object}}


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


class PlantNoteList(ResourceList):
    def query(self, view_kwargs):
        query_ = self.session.query(PlantNote)
        if view_kwargs.get('id') is not None:
            try:
                self.session.query(Plant).filter_by(id=view_kwargs['id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'}, "Plant: {} not found".format(view_kwargs['id']))
            else:
                query_ = query_.join(Plant).filter(Plant.id == view_kwargs['id'])
        return query_

    def before_create_object(self, data, view_kwargs):
        request_data = request.json

        if 'relationships' in request_data['data']:
            relationships = request_data['data']['relationships']

            if 'plant' in relationships:
                data['plant_fk'] = int(relationships['plant']['data']['id'])

    schema = PlantNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantNote,
                  'methods': {
                      'query': query,
                      'before_create_object': before_create_object
                    }
                  }


class PlantNoteDetail(ResourceDetail):
    schema = PlantNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantNote}


class PlantNoteRelationship(ResourceRelationship):
    schema = PlantNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantNote}


class PlantingPhysicalSourceList(ResourceList):
    schema = PlantingPhysicalSourceSchema
    data_layer = {'session': db.session,
                  'model': PlantingPhysicalSource}


class PlantingPhysicalSourceDetail(ResourceDetail):
    schema = PlantingPhysicalSourceSchema
    data_layer = {'session': db.session,
                  'model': PlantingPhysicalSource}


class PlantingPhysicalSourceRelationship(ResourceRelationship):
    schema = PlantingPhysicalSourceSchema
    data_layer = {'session': db.session,
                  'model': PlantingPhysicalSource}


class PlantLineageList(ResourceList):
    def query(self, view_kwargs):
        query_ = self.session.query(PlantLineage)
        if view_kwargs.get('id') is not None:
            try:
                self.session.query(Plant).filter_by(id=view_kwargs['id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'}, "Plant: {} not found".format(view_kwargs['id']))
            else:
                query_ = query_.join(Plant).filter(Plant.id == view_kwargs['id'])
        return query_

    def before_create_object(self, data, view_kwargs):
        request_data = request.json

        if 'relationships' in request_data['data']:
            relationships = request_data['data']['relationships']

            if 'plant' in relationships:
                data['plant_fk'] = int(relationships['plant']['data']['id'])

            if 'plantingphysicalsource' in relationships:
                data['planting_physical_source_fk'] = int(relationships['plantingphysicalsource']['data']['id'])

    schema = PlantLineageSchema
    data_layer = {'session': db.session,
                  'model': PlantLineage,
                  'methods': {
                      'query': query,
                      'before_create_object': before_create_object
                    }
                  }


class PlantLineageDetail(ResourceDetail):
    schema = PlantLineageSchema
    data_layer = {'session': db.session,
                  'model': PlantLineage}


class PlantLineageRelationship(ResourceRelationship):
    schema = PlantLineageSchema
    data_layer = {'session': db.session,
                  'model': PlantLineage}


class PlantGenerationList(ResourceList):
    schema = PlantGenerationSchema
    data_layer = {'session': db.session,
                  'model': PlantGeneration}


class PlantGenerationDetail(ResourceDetail):
    schema = PlantGenerationSchema
    data_layer = {'session': db.session,
                  'model': PlantGeneration}


class PlantGenerationRelationship(ResourceRelationship):
    schema = PlantGenerationSchema
    data_layer = {'session': db.session,
                  'model': PlantGeneration}


class PlantLineageGenerationList(ResourceList):
    def query(self, view_kwargs):
        query_ = self.session.query(PlantLineageGeneration)
        if view_kwargs.get('id') is not None:
            try:
                self.session.query(PlantLineage).filter_by(id=view_kwargs['id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'}, "Plant Lineage: {} not found".format(view_kwargs['id']))
            else:
                query_ = query_.join(PlantLineage).filter(PlantLineage.id == view_kwargs['id'])
        return query_

    def before_create_object(self, data, view_kwargs):
        request_data = request.json

        if 'relationships' in request_data['data']:
            relationships = request_data['data']['relationships']

            if 'plantlineage' in relationships:
                data['plant_lineage_fk'] = int(relationships['plantlineage']['data']['id'])

            if 'plantgeneration' in relationships:
                data['plant_generation'] = int(relationships['plantgeneration']['data']['id'])

    schema = PlantLineageGenerationSchema
    data_layer = {'session': db.session,
                  'model': PlantLineageGeneration,
                  'methods': {
                      'query': query,
                      'before_create_object': before_create_object
                    }
                  }


class PlantLineageGenerationDetail(ResourceDetail):
    schema = PlantLineageGenerationSchema
    data_layer = {'session': db.session,
                  'model': PlantLineageGeneration}


class PlantLineageGenerationRelationship(ResourceRelationship):
    schema = PlantLineageGenerationSchema
    data_layer = {'session': db.session,
                  'model': PlantLineageGeneration}


class PlantingList(ResourceList):
    def before_create_object(self, data, view_kwargs):
        request_data = request.json

        if 'relationships' in request_data['data']:
            relationships = request_data['data']['relationships']

            if 'plantingphysicalsource' in relationships:
                data['planting_physical_source_fk'] = int(relationships['plantingphysicalsource']['data']['id'])

            if 'plantgeneration' in relationships:
                data['plant_generation'] = int(relationships['plantgeneration']['data']['id'])

    schema = PlantingSchema
    data_layer = {'session': db.session,
                  'model': Planting,
                  'methods': {
                      'before_create_object': before_create_object
                    }
                  }


class PlantingDetail(ResourceDetail):
    schema = PlantingSchema
    data_layer = {'session': db.session,
                  'model': Planting}


class PlantingRelationship(ResourceRelationship):
    schema = PlantingSchema
    data_layer = {'session': db.session,
                  'model': Planting}


class PlantingNotesList(ResourceList):
    def before_create_object(self, data, view_kwargs):
        request_data = request.json

        if 'relationships' in request_data['data']:
            relationships = request_data['data']['relationships']

            if 'planting' in relationships:
                data['planting'] = int(relationships['planting']['data']['id'])

    schema = PlantingNotesSchema
    data_layer = {'session': db.session,
                  'model': PlantingNotes,
                  'methods': {
                      'before_create_object': before_create_object
                    }
                  }


class PlantingNotesDetail(ResourceDetail):
    schema = PlantingNotesSchema
    data_layer = {'session': db.session,
                  'model': PlantingNotes}


class PlantingNotesRelationship(ResourceRelationship):
    schema = PlantingNotesSchema
    data_layer = {'session': db.session,
                  'model': PlantingNotes}


class PlantGenerationSeedCollectionsList(ResourceList):
    def before_create_object(self, data, view_kwargs):
        request_data = request.json

        if 'relationships' in request_data['data']:
            relationships = request_data['data']['relationships']

            if 'plantgeneration' in relationships:
                data['plant_generation'] = int(relationships['plantgeneration']['data']['id'])

    schema = PlantGenerationSeedCollectionSchema
    data_layer = {'session': db.session,
                  'model': PlantGenerationSeedCollection,
                  'methods': {
                      'before_create_object': before_create_object
                    }
                  }


class PlantGenerationSeedCollectionsDetail(ResourceDetail):
    schema = PlantGenerationSeedCollection
    data_layer = {'session': db.session,
                  'model': PlantGenerationSeedCollection}


class PlantGenerationSeedCollectionsRelationship(ResourceRelationship):
    schema = PlantGenerationSeedCollection
    data_layer = {'session': db.session,
                  'model': PlantGenerationSeedCollection}


class CloningList(ResourceList):
    def before_create_object(self, data, view_kwargs):
        request_data = request.json

        if 'relationships' in request_data['data']:
            relationships = request_data['data']['relationships']

            if 'plantingphysicalsource' in relationships:
                data['planting_physical_source_fk'] = int(relationships['plantingphysicalsource']['data']['id'])

            if 'plantgeneration' in relationships:
                data['plant_generation'] = int(relationships['plantgeneration']['data']['id'])

    schema = CloningSchema
    data_layer = {'session': db.session,
                  'model': PlantCloning,
                  'methods': {
                      'before_create_object': before_create_object
                    }
                  }


class CloningDetail(ResourceDetail):
    schema = CloningSchema
    data_layer = {'session': db.session,
                  'model': PlantCloning}


class CloningRelationship(ResourceRelationship):
    schema = CloningSchema
    data_layer = {'session': db.session,
                  'model': PlantCloning}


class CloningNotesList(ResourceList):
    def before_create_object(self, data, view_kwargs):
        request_data = request.json

        if 'relationships' in request_data['data']:
            relationships = request_data['data']['relationships']

            if 'plantcloning' in relationships:
                data['plant_cloning_fk'] = int(relationships['plantcloning']['data']['id'])

    schema = CloningNotesSchema
    data_layer = {'session': db.session,
                  'model': PlantCloningNotes,
                  'methods': {
                      'before_create_object': before_create_object
                    }
                  }


class CloningNotesDetail(ResourceDetail):
    schema = CloningNotesSchema
    data_layer = {'session': db.session,
                  'model': PlantCloningNotes}


class CloningNotesRelationship(ResourceRelationship):
    schema = CloningNotesSchema
    data_layer = {'session': db.session,
                  'model': PlantCloningNotes}


class PlantHarvestList(ResourceList):
    def before_create_object(self, data, view_kwargs):
        request_data = request.json

        if 'relationships' in request_data['data']:
            relationships = request_data['data']['relationships']

            if 'plantgeneration' in relationships:
                data['plant_generation_fk'] = int(relationships['plantgeneration']['data']['id'])

    schema = PlantHarvestSchema
    data_layer = {'session': db.session,
                  'model': PlantHarvest,
                  'methods': {
                      'before_create_object': before_create_object
                    }
                  }


class PlantHarvestDetail(ResourceDetail):
    schema = PlantHarvestSchema
    data_layer = {'session': db.session,
                  'model': PlantHarvest}


class PlantHarvestRelationship(ResourceRelationship):
    schema = PlantHarvestSchema
    data_layer = {'session': db.session,
                  'model': PlantHarvest}


class PlantHarvestNotesList(ResourceList):
    def before_create_object(self, data, view_kwargs):
        request_data = request.json

        if 'relationships' in request_data['data']:
            relationships = request_data['data']['relationships']

            if 'plantharvest' in relationships:
                data['plant_harvest_fk'] = int(relationships['plantharvest']['data']['id'])

    schema = PlantHarvestNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantHarvestNotes,
                  'methods': {
                      'before_create_object': before_create_object
                    }
                  }


class PlantHarvestNotesDetail(ResourceDetail):
    schema = PlantHarvestNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantHarvestNotes}


class PlantHarvestNotesRelationship(ResourceRelationship):
    schema = PlantHarvestNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantHarvestNotes}
