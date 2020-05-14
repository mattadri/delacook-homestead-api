from app import db


class LightRequirement(db.Model):
    __tablename__ = 'light_requirement'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    light_requirement = db.Column(db.String, unique=True)
