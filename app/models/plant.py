from app import db


class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    friendly_name = db.Column(db.String, nullable=False)
    latin_name = db.Column(db.String, unique=True)
    drought_tolerant = db.Column(db.Boolean)
    medicinal = db.Column(db.Boolean)
    edible = db.Column(db.Boolean)
    image_large = db.Column(db.String)
    image_small = db.Column(db.String)
    type_fk = db.Column(db.Integer, db.ForeignKey('types.id'))
    type = db.relationship('Type', backref=db.backref('plants'))
    lifespan_fk = db.Column(db.Integer, db.ForeignKey('lifespans.id'))
    lifespan = db.relationship('LifeSpan', backref=db.backref('plants'))
    wood_type_fk = db.Column(db.Integer, db.ForeignKey('woodtypes.id'))
    wood_type = db.relationship('WoodType', backref='plants')
    leaf_cycle_fk = db.Column(db.Integer, db.ForeignKey('leafcycles.id'))
    leaf_cycle = db.relationship('LeafCycle', backref=db.backref('plants'))


# PERENNIAL, BIENNIAL, ANNUAL
class LifeSpan(db.Model):
    __tablename__ = 'lifespans'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    enum = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


# TREE, SHRUB, VEGETABLE, VINE, FLOWER
class Type(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    enum = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


# HARDWOOD OR SOFTWOOD
class WoodType(db.Model):
    __tablename__ = 'woodtypes'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    enum = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


# DECIDUOUS OR EVERGREEN
class LeafCycle(db.Model):
    __tablename__ = 'leafcycles'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    enum = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


class PlantNote(db.Model):
    __tablename__ = 'plantnotes'

    id = db.Column(db.Integer, primary_key=True)
    plant_fk = db.Column(db.Integer, db.ForeignKey('plants.id'))
    plant = db.relationship('Plant', backref=db.backref('plantnotes'))
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    note_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    note = db.Column(db.Text)


class PlantLineage(db.Model):
    __tablename__ = 'plantlineages'

    id = db.Column(db.Integer, primary_key=True)
    plant_fk = db.Column(db.Integer, db.ForeignKey('plants.id'))
    plant = db.relationship('Plant', backref=db.backref('plantlineages'))
    planting_physical_source_fk = db.Column(db.Integer, db.ForeignKey('plantingphysicalsources.id'))
    planting_physical_source = db.relationship('PlantingPhysicalSource', backref=db.backref('plantings'))
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    is_dead = db.Column(db.Boolean, default=False)
    lineage_source = db.Column(db.String) # Renee's garden, bloomer's nursery, etc.
    date_lineage_started = db.Column(db.DateTime)


class PlantLineageGeneration(db.Model):
    __tablename__ = 'plantlineagegenerations'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    plant_lineage_fk = db.Column(db.Integer, db.ForeignKey('plantlineages.id'))
    plant_lineage = db.relationship('PlantLineage', backref=db.backref('plantlineagegenerations'))
    plant_generation_fk = db.Column(db.Integer, db.ForeignKey('plantgenerations.id'))
    plant_generation = db.relationship('PlantGeneration', backref=db.backref('plantlineagegenerations'))
    generation_slot = db.Column(db.Integer, nullable=False)
    is_origin = db.Column(db.Boolean, default=False)


class PlantGeneration(db.Model):
    __tablename__ = 'plantgenerations'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class PlantGenerationSeedCollection(db.Model):
    __tablename__ = 'plantgenerationseedcollections'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    plant_generation_fk = db.Column(db.Integer, db.ForeignKey('plantgenerations.id'))
    plant_generation = db.relationship('PlantGeneration', backref=db.backref('plantgenerationseedcollections'))
    date_seeds_harvested = db.Column(db.DateTime)
    total_seeds_harvested = db.Column(db.Integer)
    date_seeds_packaged = db.Column(db.DateTime)


# A planting is an object containing data about the planting of a single generation. One generation
# could have many plantings.
class Planting(db.Model):
    __tablename__ = 'plantings'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    plant_generation_fk = db.Column(db.Integer, db.ForeignKey('plantgenerations.id'))
    plant_generation = db.relationship('PlantGeneration', backref=db.backref('generation_plantings'))
    planting_physical_source_fk = db.Column(db.Integer, db.ForeignKey('plantingphysicalsources.id'))
    planting_physical_source = db.relationship('PlantingPhysicalSource', backref=db.backref('source_plantings'))
    seeds_started = db.Column(db.Integer)
    date_seeds_started = db.Column(db.DateTime)
    starting_medium = db.Column(db.String)
    seeds_sprouted = db.Column(db.Integer)
    date_first_seeds_sprouted = db.Column(db.DateTime)
    sprouts_planted = db.Column(db.Integer)
    date_sprouts_planted = db.Column(db.DateTime)
    plants_survived = db.Column(db.Integer)
    date_next_generation_seeds_collected = db.Column(db.DateTime)


class PlantingNotes(db.Model):
    __tablename__ = 'plantingnotes'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    planting_fk = db.Column(db.Integer, db.ForeignKey('plantings.id'))
    planting = db.relationship('Planting', backref=db.backref('plantingnotes'))
    note_date = db.Column(db.DateTime)
    note = db.Column(db.Text)


# CUTTING, SEED, ROOT, BULB, UNKNOWN
class PlantingPhysicalSource(db.Model):
    __tablename__ = 'plantingphysicalsources'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    enum = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


class PlantCloning(db.Model):
    __tablename__ = 'plantclonings'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    plant_generation_fk = db.Column(db.Integer, db.ForeignKey('plantgenerations.id'))
    plant_generation = db.relationship('PlantGeneration', backref=db.backref('generation_clonings'))
    planting_physical_source_fk = db.Column(db.Integer, db.ForeignKey('plantingphysicalsources.id'))
    planting_physical_source = db.relationship('PlantingPhysicalSource', backref=db.backref('source_clonings'))
    date_cloned = db.Column(db.DateTime)
    number_cloned = db.Column(db.Integer)
    number_rooted = db.Column(db.Integer)
    date_first_plant_rooted = db.Column(db.Date)
    clones_planted = db.Column(db.Integer)
    date_clones_planted = db.Column(db.Date)
    clones_survived = db.Column(db.Integer)
    date_next_generation_seeds_collected = db.Column(db.DateTime)
    root_hormone_used = db.Column(db.Boolean)
    root_hormone_type = db.Column(db.String)
    rooting_medium = db.Column(db.String)


class PlantCloningNotes(db.Model):
    __tablename__ = 'plantcloningnotes'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    plant_cloning_fk = db.Column(db.Integer, db.ForeignKey('plantclonings.id'))
    plant_cloning = db.relationship('PlantCloning', backref=db.backref('plantcloningnotes'))
    note_date = db.Column(db.DateTime)
    note = db.Column(db.Text)


class PlantHarvest(db.Model):
    __tablename__ = 'plantharvests'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    plant_generation_fk = db.Column(db.Integer, db.ForeignKey('plantgenerations.id'))
    plant_generation = db.relationship('PlantGeneration', backref=db.backref('plantharvests'))
    start_date = db.Column(db.DateTime)
    finish_date = db.Column(db.DateTime)
    grams_harvested = db.Column(db.Integer)


class PlantHarvestNotes(db.Model):
    __tablename__ = 'plantharvestnotes'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    plant_harvest_fk = db.Column(db.Integer, db.ForeignKey('plantharvests.id'))
    plant_harvest = db.relationship('PlantHarvest', backref=db.backref('plantharvestnotes'))
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    note_date = db.Column(db.DateTime)
    note = db.Column(db.Text)


