from app import db

from app.models.plant.species import Species
from app.models.plant.category import Category
from app.models.plant.measurement_unit import MeasurementUnit
from app.models.plant.soil_fertility import SoilFertility
from app.models.plant.water_requirement import WaterRequirement
from app.models.plant.growth_habit import GrowthHabit
from app.models.plant.light_requirement import LightRequirement
from app.models.plant.use import Use

from app.models.note import Note
from app.models.season import Season


class Plant(db.Model):
    __tablename__ = 'plant'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    common_name = db.Column(db.String)
    description = db.Column(db.Text)
    sub_species = db.Column(db.String, unique=True)
    image_uri = db.Column(db.String)

    frost_tolerant = db.Column(db.Boolean, default=False)
    drought_tolerant = db.Column(db.Boolean, default=False)

    soil_ph_low = db.Column(db.Integer)
    soil_ph_high = db.Column(db.Integer)

    height = db.Column(db.Integer)
    width = db.Column(db.Integer)

    species_fk = db.Column(db.Integer, db.ForeignKey('species.id'))
    species = db.relationship(Species, foreign_keys=[species_fk], backref=db.backref('plant'))
    species_rel = db.relationship(Species, foreign_keys=[species_fk])

    category_fk = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship(Category, foreign_keys=[category_fk], backref=db.backref('plant'))
    category_rel = db.relationship(Category, foreign_keys=[category_fk])

    height_unit_fk = db.Column(db.Integer, db.ForeignKey('measurement_unit.id'))
    height_unit = db.relationship(MeasurementUnit, foreign_keys=[height_unit_fk], backref=db.backref('plant_height'))
    height_unit_rel = db.relationship(MeasurementUnit, foreign_keys=[height_unit_fk])

    width_unit_fk = db.Column(db.Integer, db.ForeignKey('measurement_unit.id'))
    width_unit = db.relationship(MeasurementUnit, foreign_keys=[width_unit_fk], backref=db.backref('plant_width'))
    width_unit_rel = db.relationship(MeasurementUnit, foreign_keys=[width_unit_fk])

    lifespan_fk = db.Column(db.Integer, db.ForeignKey('lifespan.id'))
    lifespan = db.relationship('Lifespan', foreign_keys=[lifespan_fk], backref=db.backref('plant'))
    lifespan_rel = db.relationship('Lifespan', foreign_keys=[lifespan_fk])

    soil_fk = db.Column(db.Integer, db.ForeignKey('soil.id'))
    soil = db.relationship('Soil', foreign_keys=[soil_fk], backref=db.backref('plant'))
    soil_rel = db.relationship('Soil', foreign_keys=[soil_fk])

    soil_fertility_fk = db.Column(db.Integer, db.ForeignKey('soil_fertility.id'))
    soil_fertility = db.relationship(SoilFertility, foreign_keys=[soil_fertility_fk], backref=db.backref('plant_soil_fertility'))
    soil_fertility_rel = db.relationship(SoilFertility, foreign_keys=[soil_fertility_fk])

    growth_habit_fk = db.Column(db.Integer, db.ForeignKey('growth_habit.id'))
    growth_habit = db.relationship(GrowthHabit, foreign_keys=[growth_habit_fk], backref=db.backref('plant'))
    growth_habit_rel = db.relationship(GrowthHabit, foreign_keys=[growth_habit_fk])


class PlantLightRequirement(db.Model):
    __tablename__ = 'plant_light_requirement'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_fk = db.Column(db.Integer, db.ForeignKey('plant.id'))
    plant = db.relationship('Plant', foreign_keys=[plant_fk], backref=db.backref('plant_light_requirement'))
    plant_rel = db.relationship(
        'Plant', foreign_keys=[plant_fk], backref=db.backref('light_requirement_plant_parent', cascade='all,delete'))

    light_requirement_fk = db.Column(db.Integer, db.ForeignKey('light_requirement.id'))
    light_requirement = db.relationship(
        LightRequirement,
        foreign_keys=[light_requirement_fk],
        backref=db.backref('plant_light_requirement'))
    light_requirement_rel = db.relationship(
        LightRequirement,
        foreign_keys=[light_requirement_fk], backref=db.backref('light_requirement_parent', cascade='all,delete'))


class PlantLightRequirementNote(db.Model):
    __tablename__ = 'plant_light_requirement_note'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_light_requirement_fk = db.Column(db.Integer, db.ForeignKey('plant_light_requirement.id'))
    plant_light_requirement = db.relationship(
        'PlantLightRequirement',
        foreign_keys=[plant_light_requirement_fk], backref=db.backref('plant_light_requirement_note'))
    plant_light_requirement_rel = db.relationship(
        'PlantLightRequirement',
        foreign_keys=[plant_light_requirement_fk],
        backref=db.backref('plant_light_requirement_parent', cascade='all,delete'))

    note_fk = db.Column(db.Integer, db.ForeignKey('note.id'))
    note = db.relationship(Note, foreign_keys=[note_fk], backref=db.backref('plant_light_requirement_note'))
    note_rel = db.relationship(
        Note, foreign_keys=[note_fk], backref=db.backref('light_requirement_note_parent', cascade='all,delete'))


class PlantWaterRequirement(db.Model):
    __tablename__ = 'plant_water_requirement'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_fk = db.Column(db.Integer, db.ForeignKey('plant.id'))
    plant = db.relationship('Plant', foreign_keys=[plant_fk], backref=db.backref('plant_water_requirement'))
    plant_rel = db.relationship(
        'Plant', foreign_keys=[plant_fk], backref=db.backref('water_requirement_plant_parent', cascade='all,delete'))

    water_requirement_fk = db.Column(db.Integer, db.ForeignKey('water_requirement.id'))
    water_requirement = db.relationship(
        WaterRequirement,
        foreign_keys=[water_requirement_fk],
        backref=db.backref('plant_water_requirement'))
    water_requirement_rel = db.relationship(
        WaterRequirement,
        foreign_keys=[water_requirement_fk], backref=db.backref('water_requirement_parent', cascade='all,delete'))


class PlantWaterRequirementNote(db.Model):
    __tablename__ = 'plant_water_requirement_note'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_water_requirement_fk = db.Column(db.Integer, db.ForeignKey('plant_water_requirement.id'))
    plant_water_requirement = db.relationship(
        'PlantWaterRequirement',
        foreign_keys=[plant_water_requirement_fk], backref=db.backref('plant_water_requirement_note'))
    plant_water_requirement_rel = db.relationship(
        'PlantWaterRequirement',
        foreign_keys=[plant_water_requirement_fk],
        backref=db.backref('plant_water_requirement_parent', cascade='all,delete'))

    note_fk = db.Column(db.Integer, db.ForeignKey('note.id'))
    note = db.relationship('Note', foreign_keys=[note_fk], backref=db.backref('plant_water_requirement_note'))
    note_rel = db.relationship('Note', foreign_keys=[note_fk], backref=db.backref('water_requirement_note_parent', cascade='all,delete'))


class PlantUse(db.Model):
    __tablename__ = 'plant_use'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_fk = db.Column(db.Integer, db.ForeignKey('plant.id'))
    plant = db.relationship('Plant', foreign_keys=[plant_fk], backref=db.backref('plant_use'))
    plant_rel = db.relationship(
        'Plant', foreign_keys=[plant_fk], backref=db.backref('use_plant_parent', cascade='all,delete'))

    use_fk = db.Column(db.Integer, db.ForeignKey('use.id'))
    use = db.relationship(Use, foreign_keys=[use_fk], backref=db.backref('plant_use'))
    use_rel = db.relationship(Use, foreign_keys=[use_fk], backref=db.backref('use_parent', cascade='all,delete'))


class PlantSeason(db.Model):
    __tablename__ = 'plant_season'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_fk = db.Column(db.Integer, db.ForeignKey('plant.id'))
    plant = db.relationship('Plant', foreign_keys=[plant_fk], backref=db.backref('plant_season'))
    plant_rel = db.relationship(
        'Plant', foreign_keys=[plant_fk], backref=db.backref('season_plant_parent', cascade='all,delete'))

    season_fk = db.Column(db.Integer, db.ForeignKey('season.id'))
    season = db.relationship(Season, foreign_keys=[season_fk], backref=db.backref('plant_season'))
    season_rel = db.relationship(
        Season, foreign_keys=[season_fk], backref=db.backref('season_parent', cascade='all,delete'))


class PlantNote(db.Model):
    __tablename__ = 'plant_note'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_fk = db.Column(db.Integer, db.ForeignKey('plant.id'))
    plant = db.relationship('Plant', foreign_keys=[plant_fk], backref=db.backref('plant_note'))
    plant_rel = db.relationship(
        'Plant', foreign_keys=[plant_fk], backref=db.backref('note_plant_parent', cascade='all,delete'))

    note_fk = db.Column(db.Integer, db.ForeignKey('note.id'))
    note = db.relationship(Note, foreign_keys=[note_fk], backref=db.backref('plant_note'))
    note_rel = db.relationship(Note, foreign_keys=[note_fk], backref=db.backref('note_parent', cascade='all,delete'))


class PlantPropagation(db.Model):
    __tablename__ = 'plant_propagation'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    propagation = db.Column(db.Text)

    plant_fk = db.Column(db.Integer, db.ForeignKey('plant.id'))
    plant = db.relationship('Plant', foreign_keys=[plant_fk], backref=db.backref('plant_propagation'))
    plant_rel = db.relationship(
        'Plant', foreign_keys=[plant_fk], backref=db.backref('propagation_plant_parent', cascade='all,delete'))
