from app import db

from app.models.plant.category import Category
from app.models.plant.measurement_unit import MeasurementUnit
from app.models.plant.lifespan import Lifespan
from app.models.plant.soil import Soil
from app.models.plant.soil_fertility import SoilFertility
from app.models.plant.growth_habit import GrowthHabit
from app.models.plant.light_requirement import LightRequirement
from app.models.plant.water_requirement import WaterRequirement
from app.models.plant.use import Use
from app.models.season import Season

from app.models.note import Note


class PlantChild(db.Model):
    __tablename__ = 'plant_child'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    common_name = db.Column(db.String)
    description = db.Column(db.Text)
    image_uri = db.Column(db.String)

    frost_tolerant = db.Column(db.Boolean, default=False)
    drought_tolerant = db.Column(db.Boolean, default=False)

    soil_ph_low = db.Column(db.Integer)
    soil_ph_high = db.Column(db.Integer)

    height = db.Column(db.Integer)
    width = db.Column(db.Integer)

    plant_fk = db.Column(db.Integer, db.ForeignKey('plant.id'))
    plant = db.relationship('Plant', foreign_keys=[plant_fk], backref=db.backref('plant_child'))
    plant_rel = db.relationship('Plant', foreign_keys=[plant_fk])

    category_fk = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship(Category, foreign_keys=[category_fk], backref=db.backref('plant_child'))
    category_rel = db.relationship(Category, foreign_keys=[category_fk])

    height_unit_fk = db.Column(db.Integer, db.ForeignKey('measurement_unit.id'))
    height_unit = db.relationship(MeasurementUnit, foreign_keys=[height_unit_fk], backref=db.backref('plant_child_height'))
    height_unit_rel = db.relationship(MeasurementUnit, foreign_keys=[height_unit_fk])

    width_unit_fk = db.Column(db.Integer, db.ForeignKey('measurement_unit.id'))
    width_unit = db.relationship(MeasurementUnit, foreign_keys=[width_unit_fk], backref=db.backref('plant_child_width'))
    width_unit_rel = db.relationship(MeasurementUnit, foreign_keys=[width_unit_fk])

    lifespan_fk = db.Column(db.Integer, db.ForeignKey('lifespan.id'))
    lifespan = db.relationship(Lifespan, foreign_keys=[lifespan_fk], backref=db.backref('plant_child'))
    lifespan_rel = db.relationship(Lifespan, foreign_keys=[lifespan_fk])

    soil_fk = db.Column(db.Integer, db.ForeignKey('soil.id'))
    soil = db.relationship(Soil, foreign_keys=[soil_fk], backref=db.backref('plant_child'))
    soil_rel = db.relationship(Soil, foreign_keys=[soil_fk])

    soil_fertility_fk = db.Column(db.Integer, db.ForeignKey('soil_fertility.id'))
    soil_fertility = db.relationship(SoilFertility, foreign_keys=[soil_fertility_fk],
                                     backref=db.backref('plant_child'))
    soil_fertility_rel = db.relationship(SoilFertility, foreign_keys=[soil_fertility_fk])

    growth_habit_fk = db.Column(db.Integer, db.ForeignKey('growth_habit.id'))
    growth_habit = db.relationship(GrowthHabit, foreign_keys=[growth_habit_fk], backref=db.backref('plant_child'))
    growth_habit_rel = db.relationship(GrowthHabit, foreign_keys=[growth_habit_fk])


class PlantChildLightRequirement(db.Model):
    __tablename__ = 'plant_child_light_requirement'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_child_fk = db.Column(db.Integer, db.ForeignKey('plant_child.id'))
    plant_child = db.relationship('PlantChild', foreign_keys=[plant_child_fk], backref=db.backref('plant_child_light_requirement'))
    plant_child_rel = db.relationship('PlantChild', foreign_keys=[plant_child_fk])

    light_requirement_fk = db.Column(db.Integer, db.ForeignKey('light_requirement.id'))
    light_requirement = db.relationship(
        LightRequirement,
        foreign_keys=[light_requirement_fk],
        backref=db.backref('plant_child_light_requirement'))
    light_requirement_rel = db.relationship(LightRequirement, foreign_keys=[light_requirement_fk])


class PlantChildLightRequirementNote(db.Model):
    __tablename__ = 'plant_child_light_requirement_note'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_child_light_requirement_fk = db.Column(db.Integer, db.ForeignKey('plant_child_light_requirement.id'))
    plant_child_light_requirement = db.relationship('PlantChildLightRequirement', foreign_keys=[plant_child_light_requirement_fk], backref=db.backref('plant_child_light_requirement_note'))
    plant_child_light_requirement_rel = db.relationship('PlantChildLightRequirement', foreign_keys=[plant_child_light_requirement_fk])

    note_fk = db.Column(db.Integer, db.ForeignKey('note.id'))
    note = db.relationship(Note, foreign_keys=[note_fk], backref=db.backref('plant_child_light_requirement_note'))
    note_rel = db.relationship(Note, foreign_keys=[note_fk])


class PlantChildWaterRequirement(db.Model):
    __tablename__ = 'plant_child_water_requirement'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_child_fk = db.Column(db.Integer, db.ForeignKey('plant_child.id'))
    plant_child = db.relationship('PlantChild', foreign_keys=[plant_child_fk],
                                  backref=db.backref('plant_child_water_requirement'))
    plant_child_rel = db.relationship('PlantChild', foreign_keys=[plant_child_fk])

    water_child_requirement_fk = db.Column(db.Integer, db.ForeignKey('water_requirement.id'))
    water_child_requirement = db.relationship(
        WaterRequirement,
        foreign_keys=[water_child_requirement_fk],
        backref=db.backref('plant_child_water_requirement'))
    water_child_requirement_rel = db.relationship(WaterRequirement, foreign_keys=[water_child_requirement_fk])


class PlantChildWaterRequirementNote(db.Model):
    __tablename__ = 'plant_child_water_requirement_note'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_child_water_requirement_fk = db.Column(db.Integer, db.ForeignKey('plant_child_water_requirement.id'))
    plant_child_water_requirement = db.relationship('PlantChildWaterRequirement', foreign_keys=[plant_child_water_requirement_fk], backref=db.backref('plant_child_water_requirement_note'))
    plant_child_water_requirement_rel = db.relationship('PlantChildWaterRequirement', foreign_keys=[plant_child_water_requirement_fk])

    note_fk = db.Column(db.Integer, db.ForeignKey('note.id'))
    note = db.relationship('Note', foreign_keys=[note_fk], backref=db.backref('plant_child_water_requirement_note'))
    note_rel = db.relationship('Note', foreign_keys=[note_fk])


class PlantChildUse(db.Model):
    __tablename__ = 'plant_child_use'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_child_fk = db.Column(db.Integer, db.ForeignKey('plant_child.id'))
    plant_child = db.relationship('PlantChild', foreign_keys=[plant_child_fk],
                                  backref=db.backref('plant_child_use'))
    plant_child_rel = db.relationship('PlantChild', foreign_keys=[plant_child_fk])

    use_fk = db.Column(db.Integer, db.ForeignKey('use.id'))
    use = db.relationship(Use, foreign_keys=[use_fk], backref=db.backref('plant_child_use'))
    use_rel = db.relationship(Use, foreign_keys=[use_fk])


class PlantChildSeason(db.Model):
    __tablename__ = 'plant_child_season'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_child_fk = db.Column(db.Integer, db.ForeignKey('plant_child.id'))
    plant_child = db.relationship('PlantChild', foreign_keys=[plant_child_fk],
                                  backref=db.backref('plant_child_season'))
    plant_child_rel = db.relationship('PlantChild', foreign_keys=[plant_child_fk])

    season_fk = db.Column(db.Integer, db.ForeignKey('season.id'))
    season = db.relationship(Season, foreign_keys=[season_fk], backref=db.backref('plant_child_season'))
    season_rel = db.relationship(Season, foreign_keys=[season_fk])


class PlantChildNote(db.Model):
    __tablename__ = 'plant_child_note'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    plant_child_fk = db.Column(db.Integer, db.ForeignKey('plant_child.id'))
    plant_child = db.relationship('PlantChild', foreign_keys=[plant_child_fk],
                                  backref=db.backref('plant_child_note'))
    plant_child_rel = db.relationship('PlantChild', foreign_keys=[plant_child_fk])

    note_fk = db.Column(db.Integer, db.ForeignKey('note.id'))
    note = db.relationship(Note, foreign_keys=[note_fk], backref=db.backref('plant_child_note'))
    note_rel = db.relationship(Note, foreign_keys=[note_fk])


class PlantChildPropagation(db.Model):
    __tablename__ = 'plant_child_propagation'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    propagation = db.Column(db.Text)

    plant_child_fk = db.Column(db.Integer, db.ForeignKey('plant_child.id'))
    plant_child = db.relationship('PlantChild', foreign_keys=[plant_child_fk],
                                  backref=db.backref('plant_child_propagation'))
    plant_child_rel = db.relationship('PlantChild', foreign_keys=[plant_child_fk])
