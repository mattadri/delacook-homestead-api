from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from app import db
from app.models.season import Season


class SeasonSchema(Schema):
    class Meta:
        type_ = 'season'
        self_view = 'season_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'season_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)


class SeasonList(ResourceList):
    schema = SeasonSchema
    data_layer = {'session': db.session,
                  'model': Season}


class SeasonDetail(ResourceDetail):
    schema = SeasonSchema
    data_layer = {'session': db.session,
                  'model': Season}
