from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from app import db
from app.models.plant.lifespan import Lifespan


class LifespanSchema(Schema):
    class Meta:
        type_ = 'lifespan'
        self_view = 'lifespan_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'lifespan_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)


class LifespanList(ResourceList):
    schema = LifespanSchema
    data_layer = {'session': db.session,
                  'model': Lifespan}


class LifespanDetail(ResourceDetail):
    schema = LifespanSchema
    data_layer = {'session': db.session,
                  'model': Lifespan}
