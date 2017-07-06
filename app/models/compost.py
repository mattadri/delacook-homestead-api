from app import db


class CompostPile(db.Model):
    __tablename__ = 'compostpiles'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    label = db.Column(db.String)
    started = db.Column(db.Date)
    finished = db.Column(db.Date)
    is_active = db.Column(db.Boolean)


class CompostPileHistory(db.Model):
    __tablename__ = 'compostpilehistories'

    id = db.Column(db.Integer, primary_key=True)
    compost_pile_fk = db.Column(db.Integer, db.ForeignKey('compostpiles.id'))
    compost_pile = db.relationship('CompostPile', backref=db.backref('compostpilehistories'))
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    date = db.Column(db.Date)
    temperature = db.Column(db.Integer)
    moisture = db.Column(db.Integer)
    turned = db.Column(db.Boolean)
    scraps_added = db.Column(db.Boolean)
