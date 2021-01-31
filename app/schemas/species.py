from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema, Relationship

from app import db

from app.models.plant.species import Species


class SpeciesSchema(Schema):
    class Meta:
        type_ = 'species'
        self_view = 'species_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'species_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)

    genus = fields.Nested('GenusSchema')

    genus_rel = Relationship(
        schema='GenusSchema',
        type_='genus'
    )


class SpeciesList(ResourceList):
    schema = SpeciesSchema
    data_layer = {'session': db.session,
                  'model': Species}


class SpeciesDetail(ResourceDetail):
    schema = SpeciesSchema
    data_layer = {'session': db.session,
                  'model': Species}
