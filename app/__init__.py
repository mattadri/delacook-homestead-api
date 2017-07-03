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
    from app.schemas import RainfallTotalList, RainfallTotalDetail
    from app.schemas import CompostPileList, CompostPileDetail, CompostPileRelationship
    from app.schemas import CompostPileHistoryList, CompostPileHistoryDetail, CompostPileHistoryRelationship

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
