from app import db

from app.models.plant.family import Family


class Genus(db.Model):
    __tablename__ = 'genus'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    label = db.Column(db.String)
    description = db.Column(db.Text)

    family_fk = db.Column(db.Integer, db.ForeignKey('family.id'))
    family = db.relationship(Family, foreign_keys=[family_fk], backref=db.backref('genus'))
    family_rel = db.relationship(Family, foreign_keys=[family_fk])
