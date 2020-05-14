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

    from app.schemas.garden import GardenList, GardenDetail, GardenBedList, GardenBedDetail
    from app.schemas.bed import BedList, BedDetail, BedPlantList, BedPlantDetail
    from app.schemas.plant import PlantList, PlantDetail, PlantVarietyList, PlantVarietyDetail
    from app.schemas.lifespan import LifespanList, LifespanDetail
    from app.schemas.soil import SoilList, SoilDetail

    api = Api(flask_app)

    api.route(GardenList, 'garden_list', '/gardens')
    api.route(GardenDetail, 'garden_detail', '/gardens/<int:id>')

    api.route(BedList, 'bed_list', '/beds')
    api.route(BedDetail, 'bed_detail', '/beds/<int:id>')

    api.route(LifespanList, 'lifespan_list', '/lifespans')
    api.route(LifespanDetail, 'lifespan_detail', '/lifespans/<int:id>')

    api.route(SoilList, 'soil_list', '/soils')
    api.route(SoilDetail, 'soil_detail', '/soils/<int:id>')

    api.route(PlantList, 'plant_list', '/plants')
    api.route(PlantDetail, 'plant_detail', '/plants/<int:id>')

    api.route(PlantVarietyList, 'variety_list', '/varieties')
    api.route(PlantVarietyDetail, 'variety_detail', '/varieties/<int:id>')

    api.route(GardenBedList, 'garden_bed_list', '/garden_beds')
    api.route(GardenBedDetail, 'garden_bed_detail', '/garden_beds/<int:id>')

    api.route(BedPlantList, 'bed_plant_list', '/bed_plants')
    api.route(BedPlantDetail, 'bed_plant_detail', '/bed_plants/<int:id>')


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
