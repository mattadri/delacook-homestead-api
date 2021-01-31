from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from app import db
from app.models.plant.category import Category


class CategorySchema(Schema):
    class Meta:
        type_ = 'category'
        self_view = 'category_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'category_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)


class CategoryList(ResourceList):
    schema = CategorySchema
    data_layer = {'session': db.session,
                  'model': Category}


class CategoryDetail(ResourceDetail):
    schema = CategorySchema
    data_layer = {'session': db.session,
                  'model': Category}
