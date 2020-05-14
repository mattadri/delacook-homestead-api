from app import db


class Garden(db.Model):
    __tablename__ = 'garden'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    label = db.Column(db.String)


class GardenBed(db.Model):
    __tablename__ = 'garden_bed'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    garden_fk = db.Column(db.Integer, db.ForeignKey('garden.id'))
    garden = db.relationship('Garden', foreign_keys=[garden_fk], backref=db.backref('garden_bed'))
    garden_rel = db.relationship('Garden', foreign_keys=[garden_fk])

    bed_fk = db.Column(db.Integer, db.ForeignKey('bed.id'))
    bed = db.relationship('Bed', foreign_keys=[bed_fk], backref=db.backref('garden_bed'))
    bed_rel = db.relationship('Bed', foreign_keys=[bed_fk])
