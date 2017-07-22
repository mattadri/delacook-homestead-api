import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# local config import
from instance.config import app_config


db = SQLAlchemy()


# noinspection PyTypeChecker
def create_api(flask_app):
    from flask_rest_jsonapi import Api
    from app.schemas.rainfall import RainfallTotalList, RainfallTotalDetail
    from app.schemas.compost import CompostPileList, CompostPileDetail, CompostPileRelationship
    from app.schemas.compost import CompostPileHistoryList, CompostPileHistoryDetail, CompostPileHistoryRelationship
    from app.schemas.plant import PlantList, PlantDetail, PlantRelationship
    from app.schemas.plant import TypeList, TypeDetail, TypeRelationship
    from app.schemas.plant import WoodTypeList, WoodTypeDetail, WoodTypeRelationship
    from app.schemas.plant import LifeSpanList, LifeSpanDetail, LifeSpanRelationship
    from app.schemas.plant import LeafCycleList, LeafCycleDetail, LeafCycleRelationship
    from app.schemas.plant import PlantNoteList, PlantNoteDetail, PlantNoteRelationship

    api = Api(flask_app)

    # RAINFALL TOTALS ROUTES
    api.route(RainfallTotalList, 'rainfall_total_list',
              '/rainfalltotals')

    api.route(RainfallTotalDetail, 'rainfall_total_detail',
              '/rainfalltotals/<int:id>')

    # COMPOST PILE ROUTES
    api.route(CompostPileList, 'compost_pile_list',
              '/compostpiles')

    api.route(CompostPileDetail, 'compost_pile_detail',
              '/compostpiles/<int:id>',
              '/compostpilehistories/<int:compost_pile_history_id>/compostpile')

    api.route(CompostPileRelationship, 'compost_pile_histories',
              '/compostpiles/<int:id>/relationships/compostpilehistories')

    api.route(CompostPileHistoryList, 'compost_pile_history_list',
              '/compostpilehistories',
              '/compostpiles/<int:id>/compostpilehistories')

    api.route(CompostPileHistoryDetail, 'compost_pile_history_detail',
              '/compostpilehistories/<int:id>')

    api.route(CompostPileHistoryRelationship, 'history_compost_pile',
              '/compostpilehistories/<int:id>/relationships/compostpile')

    # PLANT ROUTES
    api.route(PlantList, 'plant_list',
              '/plants')

    api.route(PlantDetail, 'plant_detail',
              '/plants/<int:id>',
              '/plantnotes/<int:plant_note_id>/plant')

    api.route(PlantRelationship, 'plant_lifespan',
              '/plants/<int:id>/relationships/lifespans')

    api.route(PlantRelationship, 'plant_type',
              '/plants/<int:id>/relationships/types')

    api.route(PlantRelationship, 'plant_wood_type',
              '/plants/<int:id>/relationships/woodtypes')

    api.route(PlantRelationship, 'plant_leaf_cycle',
              '/plants/<int:id>/relationships/leafcycles')

    api.route(PlantRelationship, 'plant_notes',
              '/plants/<int:id>/relationships/notes')

    api.route(TypeList, 'type_list',
              '/types')

    api.route(TypeDetail, 'type_detail',
              '/types/<int:id>')

    api.route(TypeRelationship, 'type_plant',
              '/types/<int:id>/relationships/plants')

    api.route(WoodTypeList, 'woodtype_list',
              '/woodtypes')

    api.route(WoodTypeDetail, 'woodtype_detail',
              '/woodtypes/<int:id>')

    api.route(WoodTypeRelationship, 'woodtype_plant',
              '/woodtypes/<int:id>/relationships/plants')

    api.route(LifeSpanList, 'lifespan_list',
              '/lifespans')

    api.route(LifeSpanDetail, 'lifespan_detail',
              '/lifespans/<int:id>')

    api.route(LifeSpanRelationship, 'lifespan_plant',
              '/lifespans/<int:id>/relationships/plants')

    api.route(LeafCycleList, 'leafcycle_list',
              '/leafcycles')

    api.route(LeafCycleDetail, 'leafcycle_detail',
              '/leafcycles/<int:id>')

    api.route(LeafCycleRelationship, 'leafcycle_plant',
              '/leafcycles/<int:id>/relationships/plants')

    api.route(PlantNoteList, 'plantnote_list',
              '/plantnotes',
              '/plants/<int:id>/plantnotes')

    api.route(PlantNoteDetail, 'plantnote_detail',
              '/plantnotes/<int:id>')

    api.route(PlantNoteRelationship, 'plantnote_plant',
              '/plantnotes/<int:id>/relationships/plant')


def create_flask_app(environment_config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(app_config[environment_config])
    flask_app.config.from_pyfile('../instance/config.py')
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(flask_app)

    return flask_app


def create_app(environment_config):
    app = create_flask_app(environment_config)
    create_api(app)
    db.init_app(app)

    return app

config_name = os.getenv('APP_SETTINGS')
application = create_app(config_name)
