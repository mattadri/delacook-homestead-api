from flask import request

from sqlalchemy.orm.exc import NoResultFound

from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from flask_rest_jsonapi.exceptions import ObjectNotFound

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

from app import db
from app.models.compost import CompostPile, CompostPileHistory


# COMPOST PILES
class CompostPileSchema(Schema):
    class Meta:
        type_ = 'compostpiles'
        self_view = 'compost_pile_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'compost_pile_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    started = fields.Date()
    finished = fields.Date()
    label = fields.Str(required=True)
    isactive = fields.Boolean(attribute='is_active')
    compostpilehistories = Relationship(
        self_view='compost_pile_histories',
        self_view_kwargs={'id': '<id>'},
        related_view='compost_pile_history_list',
        related_view_kwargs={'id': '<id>'},
        many=True,
        schema='CompostHistorySchema',
        type_='compostpilehistories')


class CompostHistorySchema(Schema):
    class Meta:
        type_ = 'compostpilehistories'
        self_view = 'compost_pile_history_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'compost_pile_history_list'

    id = fields.Str(dump_only=True)
    created = fields.Date()
    modified = fields.Date()
    date = fields.Date()
    temperature = fields.Integer()
    moisture = fields.Integer()
    turned = fields.Boolean()
    scrapsadded = fields.Boolean(attribute='scraps_added')
    compostpile = Relationship(
        attribute='compost_pile',
        self_view='history_compost_pile',
        self_view_kwargs={'id': '<id>'},
        related_view='compost_pile_detail',
        related_view_kwargs={'compost_pile_history_id': '<id>'},
        schema='CompostPileSchema',
        type_='compostpiles')


class CompostPileList(ResourceList):
    schema = CompostPileSchema
    data_layer = {'session': db.session,
                  'model': CompostPile}


class CompostPileDetail(ResourceDetail):
    def before_get_object(self, view_kwargs):
        if view_kwargs.get('compost_pile_history_id') is not None:
            try:
                compost_pile_history = self.session.query(CompostPileHistory).filter_by(
                    id=view_kwargs['compost_pile_history_id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'compost_pile_history_id'},
                                     "Compost Pile History: {} not found".format(
                                         view_kwargs['compost_pile_history_id']))
            else:
                if compost_pile_history.compost_pile is not None:
                    view_kwargs['id'] = compost_pile_history.compost_pile.id
                else:
                    view_kwargs['id'] = None

    schema = CompostPileSchema
    data_layer = {'session': db.session,
                  'model': CompostPile,
                  'methods': {'before_get_object': before_get_object}}


class CompostPileRelationship(ResourceRelationship):
    schema = CompostPileSchema
    data_layer = {'session': db.session,
                  'model': CompostPile}


class CompostPileHistoryList(ResourceList):
    def query(self, view_kwargs):
        query_ = self.session.query(CompostPileHistory)
        if view_kwargs.get('id') is not None:
            try:
                self.session.query(CompostPile).filter_by(id=view_kwargs['id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'}, "Person: {} not found".format(view_kwargs['id']))
            else:
                query_ = query_.join(CompostPile).filter(CompostPile.id == view_kwargs['id'])
        return query_

    def before_create_object(self, data, view_kwargs):
        if view_kwargs.get('id') is not None:
            compost_pile = self.session.query(CompostPile).filter_by(id=view_kwargs['id']).one()
            data['compost_pile_fk'] = compost_pile.id

        else:
            request_data = request.json

            if 'relationships' in request_data['data']:
                relationships = request_data['data']['relationships']

                if 'compostpile' in relationships:
                    data['compost_pile_fk'] = int(relationships['compostpile']['data']['id'])

    schema = CompostHistorySchema
    data_layer = {
        'session': db.session,
        'model': CompostPileHistory,
        'methods': {
            'query': query,
            'before_create_object': before_create_object
        }
    }


class CompostPileHistoryDetail(ResourceDetail):
    schema = CompostHistorySchema
    data_layer = {'session': db.session,
                  'model': CompostPileHistory}


class CompostPileHistoryRelationship(ResourceRelationship):
    schema = CompostHistorySchema
    data_layer = {'session': db.session,
                  'model': CompostPileHistory}
