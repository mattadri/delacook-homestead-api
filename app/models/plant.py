from app import db


class Plant(db.Model):
    __tablename__ = 'plant'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    common_name = db.Column(db.String)
    latin_name = db.Column(db.String, unique=True)

    lifespan_fk = db.Column(db.Integer, db.ForeignKey('lifespan.id'))
    lifespan = db.relationship('Lifespan', foreign_keys=[lifespan_fk], backref=db.backref('plant'))
    lifespan_rel = db.relationship('Lifespan', foreign_keys=[lifespan_fk])

    soil_fk = db.Column(db.Integer, db.ForeignKey('soil.id'))
    soil = db.relationship('Soil', foreign_keys=[soil_fk], backref=db.backref('plant'))
    soil_rel = db.relationship('Soil', foreign_keys=[soil_fk])


class PlantVariety(db.Model):
    __tablename__ = 'plant_variety'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    label = db.Column(db.String)

    plant_fk = db.Column(db.Integer, db.ForeignKey('plant.id'))
    plant = db.relationship('Plant', foreign_keys=[plant_fk], backref=db.backref('plant_variety'))
    plant_rel = db.relationship('Plant', foreign_keys=[plant_fk])

    lifespan_fk = db.Column(db.Integer, db.ForeignKey('lifespan.id'))
    lifespan = db.relationship('Lifespan', foreign_keys=[lifespan_fk], backref=db.backref('plant_variety'))
    lifespan_rel = db.relationship('Lifespan', foreign_keys=[lifespan_fk])

    soil_fk = db.Column(db.Integer, db.ForeignKey('soil.id'))
    soil = db.relationship('Soil', foreign_keys=[soil_fk], backref=db.backref('plant_variety'))
    soil_rel = db.relationship('Soil', foreign_keys=[soil_fk])
