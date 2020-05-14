from app import db


class Bed(db.Model):
    __tablename__ = 'bed'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    label = db.Column(db.String)


class BedPlant(db.Model):
    __tablename__ = 'bed_plant'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    bed_fk = db.Column(db.Integer, db.ForeignKey('bed.id'))
    bed = db.relationship('Bed', foreign_keys=[bed_fk], backref=db.backref('bed_plant'))
    bed_rel = db.relationship('Bed', foreign_keys=[bed_fk])

    plant_fk = db.Column(db.Integer, db.ForeignKey('plant.id'))
    plant = db.relationship('Plant', foreign_keys=[plant_fk], backref=db.backref('bed_plant'))
    plant_rel = db.relationship('Plant', foreign_keys=[plant_fk])
