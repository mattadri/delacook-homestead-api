from app import db


class RainfallTotal(db.Model):
    __tablename__ = 'rainfalltotals'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    date = db.Column(db.Date)
    amount = db.Column(db.Float)
