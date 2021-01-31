from app import db


class MeasurementUnit(db.Model):
    __tablename__ = 'measurement_unit'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    label_singular = db.Column(db.String)
    label_plural = db.Column(db.String)

