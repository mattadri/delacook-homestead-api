from app import db

from app.models.plant.genus import Genus


class Species(db.Model):
    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    label = db.Column(db.String)

    genus_fk = db.Column(db.Integer, db.ForeignKey('genus.id'))
    genus = db.relationship(Genus, foreign_keys=[genus_fk], backref=db.backref('species'))
    genus_rel = db.relationship(Genus, foreign_keys=[genus_fk])
