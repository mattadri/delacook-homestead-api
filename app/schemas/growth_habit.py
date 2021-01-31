from flask_rest_jsonapi import ResourceDetail, ResourceList
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from app import db
from app.models.plant.growth_habit import GrowthHabit


class GrowthHabitSchema(Schema):
    class Meta:
        type_ = 'growth_habit'
        self_view = 'growth_habit_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'growth_habit_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    label = fields.String(required=True)


class GrowthHabitList(ResourceList):
    schema = GrowthHabitSchema
    data_layer = {'session': db.session,
                  'model': GrowthHabit}


class GrowthHabitDetail(ResourceDetail):
    schema = GrowthHabitSchema
    data_layer = {'session': db.session,
                  'model': GrowthHabit}
