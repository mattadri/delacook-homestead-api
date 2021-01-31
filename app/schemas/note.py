from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from app import db
from app.models.note import Note


class NoteSchema(Schema):
    class Meta:
        type_ = 'note'
        self_view = 'note_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'note_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    text = fields.String(required=True)


class NoteList(ResourceList):
    schema = NoteSchema
    data_layer = {'session': db.session,
                  'model': Note}


class NoteDetail(ResourceDetail):
    schema = NoteSchema
    data_layer = {'session': db.session,
                  'model': Note}
