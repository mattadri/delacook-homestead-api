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


# TREE, SHRUB, FLOWER, GRASS
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
