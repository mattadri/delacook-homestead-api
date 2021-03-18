from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema, Relationship

from app import db
from app.models.plant.plant import Plant, PlantNote, PlantLightRequirement, PlantLightRequirementNote, \
    PlantWaterRequirement, PlantWaterRequirementNote, PlantUse, PlantPropagation, PlantSeason


# PLANT
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

    species = fields.Nested('SpeciesSchema')
    category = fields.Nested('CategorySchema')
    height_unit = fields.Nested('MeasurementUnitSchema')
    width_unit = fields.Nested('MeasurementUnitSchema')
    lifespan = fields.Nested('LifespanSchema')
    soil = fields.Nested('SoilSchema')
    soil_fertility = fields.Nested('SoilFertilitySchema')
    growth_habit = fields.Nested('GrowthHabitSchema')

    plant_note = fields.Nested('PlantNoteSchema', many=True, exclude=('plant',))
    plant_use = fields.Nested('PlantUseSchema', many=True, exclude=('plant',))
    plant_season = fields.Nested('PlantSeasonSchema', many=True, exclude=('plant',))
    plant_propagation = fields.Nested('PlantPropagationSchema', many=True, exclude=('plant',))
    plant_light_requirement = fields.Nested('PlantLightRequirementSchema', many=True, exclude=('plant',))
    plant_water_requirement = fields.Nested('PlantWaterRequirementSchema', many=True, exclude=('plant',))

    species_rel = Relationship(
        schema='SpeciesSchema',
        type_='species',
        required=False
    )

    category_rel = Relationship(
        schema='CategorySchema',
        type_='category',
        required=False
    )

    height_unit_rel = Relationship(
        schema='MeasurementUnitSchema',
        type_='measurement_unit',
        required=False
    )

    width_unit_rel = Relationship(
        schema='MeasurementUnitSchema',
        type_='measurement_unit',
        required=False
    )

    lifespan_rel = Relationship(
        schema='LifespanSchema',
        type_='lifespan',
        required=False
    )

    soil_rel = Relationship(
        schema='SoilSchema',
        type_='soil',
        required=False
    )

    soil_fertility_rel = Relationship(
        schema='SoilFertilitySchema',
        type_='soil_fertility',
        required=False
    )

    growth_habit_rel = Relationship(
        schema='GrowthHabitSchema',
        type_='growth_habit',
        required=False
    )


class PlantList(ResourceList):
    schema = PlantSchema
    data_layer = {'session': db.session,
                  'model': Plant}


class PlantDetail(ResourceDetail):
    schema = PlantSchema
    data_layer = {'session': db.session,
                  'model': Plant}


# PLANT LIGHT REQUIREMENT
class PlantLightRequirementSchema(Schema):
    class Meta:
        type_ = 'plant_light_requirement'
        self_view = 'plant_light_requirement_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plant_light_requirement_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    plant = fields.Nested('PlantSchema')
    light_requirement = fields.Nested('LightRequirementSchema')
    plant_light_requirement_note = fields.Nested('PlantLightRequirementNoteSchema', many=True)

    plant_rel = Relationship(
        schema='PlantSchema',
        type_='plant',
        required=True
    )

    light_requirement_rel = Relationship(
        schema='LightRequirementSchema',
        type_='light_requirement',
        required=True
    )


class PlantLightRequirementList(ResourceList):
    schema = PlantLightRequirementSchema
    data_layer = {'session': db.session,
                  'model': PlantLightRequirement}


class PlantLightRequirementDetail(ResourceDetail):
    schema = PlantLightRequirementSchema
    data_layer = {'session': db.session,
                  'model': PlantLightRequirement}


# PLANT LIGHT REQUIREMENT NOTE
class PlantLightRequirementNoteSchema(Schema):
    class Meta:
        type_ = 'plant_light_requirement_note'
        self_view = 'plant_light_requirement_note_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plant_light_requirement_note_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    light_requirement = fields.Nested('LightRequirementSchema')
    note = fields.Nested('NoteSchema')

    plant_light_requirement_rel = Relationship(
        schema='LightRequirementSchema',
        type_='plant_light_requirement',
        required=True
    )

    note_rel = Relationship(
        schema='NoteSchema',
        type_='note',
        required=True
    )


class PlantLightRequirementNoteList(ResourceList):
    schema = PlantLightRequirementNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantLightRequirementNote}


class PlantLightRequirementNoteDetail(ResourceDetail):
    schema = PlantLightRequirementNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantLightRequirementNote}


# PLANT WATER REQUIREMENT
class PlantWaterRequirementSchema(Schema):
    class Meta:
        type_ = 'plant_water_requirement'
        self_view = 'plant_water_requirement_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plant_water_requirement_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    plant = fields.Nested('PlantSchema')
    water_requirement = fields.Nested('WaterRequirementSchema')
    plant_water_requirement_note = fields.Nested('PlantWaterRequirementNoteSchema', many=True)

    plant_rel = Relationship(
        schema='PlantSchema',
        type_='plant',
        required=True
    )

    water_requirement_rel = Relationship(
        schema='WaterRequirementSchema',
        type_='water_requirement',
        required=True
    )


class PlantWaterRequirementList(ResourceList):
    schema = PlantWaterRequirementSchema
    data_layer = {'session': db.session,
                  'model': PlantWaterRequirement}


class PlantWaterRequirementDetail(ResourceDetail):
    schema = PlantWaterRequirementSchema
    data_layer = {'session': db.session,
                  'model': PlantWaterRequirement}


# PLANT WATER REQUIREMENT NOTE
class PlantWaterRequirementNoteSchema(Schema):
    class Meta:
        type_ = 'plant_water_requirement_note'
        self_view = 'plant_water_requirement_note_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plant_water_requirement_note_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    water_requirement = fields.Nested('WaterRequirementSchema')
    note = fields.Nested('NoteSchema')

    plant_water_requirement_rel = Relationship(
        schema='WaterRequirementSchema',
        type_='plant_water_requirement',
        required=True
    )

    note_rel = Relationship(
        schema='NoteSchema',
        type_='note',
        required=True
    )


class PlantWaterRequirementNoteList(ResourceList):
    schema = PlantWaterRequirementNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantWaterRequirementNote}


class PlantWaterRequirementNoteDetail(ResourceDetail):
    schema = PlantWaterRequirementNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantWaterRequirementNote}


# PLANT NOTE
class PlantNoteSchema(Schema):
    class Meta:
        type_ = 'plant_note'
        self_view = 'plant_note_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plant_note_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    plant = fields.Nested('PlantSchema')
    note = fields.Nested('NoteSchema')

    plant_rel = Relationship(
        schema='PlantSchema',
        type_='plant',
        required=True
    )

    note_rel = Relationship(
        schema='NoteSchema',
        type_='note',
        required=True
    )


class PlantNoteList(ResourceList):
    schema = PlantNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantNote}


class PlantNoteDetail(ResourceDetail):
    schema = PlantNoteSchema
    data_layer = {'session': db.session,
                  'model': PlantNote}


# PLANT USE
class PlantUseSchema(Schema):
    class Meta:
        type_ = 'plant_use'
        self_view = 'plant_use_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plant_use_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    plant = fields.Nested('PlantSchema')
    use = fields.Nested('UseSchema')

    plant_rel = Relationship(
        schema='PlantSchema',
        type_='plant',
        required=True
    )

    use_rel = Relationship(
        schema='UseSchema',
        type_='use',
        required=True
    )


class PlantUseList(ResourceList):
    schema = PlantUseSchema
    data_layer = {'session': db.session,
                  'model': PlantUse}


class PlantUseDetail(ResourceDetail):
    schema = PlantUseSchema
    data_layer = {'session': db.session,
                  'model': PlantUse}


# PLANT SEASON
class PlantSeasonSchema(Schema):
    class Meta:
        type_ = 'plant_season'
        self_view = 'plant_season_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plant_season_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    plant = fields.Nested('PlantSchema')
    season = fields.Nested('SeasonSchema')

    plant_rel = Relationship(
        schema='PlantSchema',
        type_='plant',
        required=True
    )

    season_rel = Relationship(
        schema='SeasonSchema',
        type_='season',
        required=True
    )


class PlantSeasonList(ResourceList):
    schema = PlantSeasonSchema
    data_layer = {'session': db.session,
                  'model': PlantSeason}


class PlantSeasonDetail(ResourceDetail):
    schema = PlantSeasonSchema
    data_layer = {'session': db.session,
                  'model': PlantSeason}


# PLANT PROPAGATION
class PlantPropagationSchema(Schema):
    class Meta:
        type_ = 'plant_propagation'
        self_view = 'plant_propagation_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'plant_propagation_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()

    propagation = fields.String()

    plant = fields.Nested('PlantSchema')

    plant_rel = Relationship(
        schema='PlantSchema',
        type_='plant',
        required=True
    )


class PlantPropagationList(ResourceList):
    schema = PlantPropagationSchema
    data_layer = {'session': db.session,
                  'model': PlantPropagation}


class PlantPropagationDetail(ResourceDetail):
    schema = PlantPropagationSchema
    data_layer = {'session': db.session,
                  'model': PlantPropagation}
