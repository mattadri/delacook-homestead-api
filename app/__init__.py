from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# local config import
from instance.config import app_config


db = SQLAlchemy()


# noinspection PyTypeChecker
def create_api(flask_app):
    from flask_rest_jsonapi import Api
    from app.schemas import CompostPileList, CompostPileDetail, CompostPileRelationship
    from app.schemas import CompostPileHistoryList, CompostPileHistoryDetail, CompostPileHistoryRelationship

    api = Api(flask_app)

    api.route(CompostPileList, 'compost_pile_list',
              '/compostpiles')

    api.route(CompostPileDetail, 'compost_pile_detail',
              '/compostpiles/<int:id>',
              '/compostpilehistories/<int:compost_pile_history_id>/compost-pile')

    api.route(CompostPileRelationship, 'compost_pile_histories',
              '/compostpiles/<int:id>/relationships/histories')

    api.route(CompostPileHistoryList, 'compost_pile_history_list',
              '/compostpilehistories',
              '/compostpiles/<int:id>/compost-pile-histories')

    api.route(CompostPileHistoryDetail, 'compost_pile_history_detail',
              '/compostpilehistories/<int:id>')

    api.route(CompostPileHistoryRelationship, 'history_compost_pile',
              '/compostpilehistories/<int:id>/relationships/compost_pile')


def create_flask_app(config_name):
    flask_app = Flask(__name__)
    flask_app.config.from_object(app_config[config_name])
    flask_app.config.from_pyfile('../instance/config.py')
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(flask_app)

    return flask_app


def create_app(config_name):
    app = create_flask_app(config_name)
    create_api(app)
    db.init_app(app)

    return app
