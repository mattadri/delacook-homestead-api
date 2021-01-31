from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from app import db
from app.models.plant.use import Use


class UseSchema(Schema):
    class Meta:
        type_ = 'use'
        self_view = 'use_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'use_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    text = fields.String(required=True)


class UseList(ResourceList):
    schema = UseSchema
    data_layer = {'session': db.session,
                  'model': Use}


class UseDetail(ResourceDetail):
    schema = UseSchema
    data_layer = {'session': db.session,
                  'model': Use}
