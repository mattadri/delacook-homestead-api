import os

from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import uuid

import boto3

# local config import
from instance.config import app_config

db = SQLAlchemy()

s3 = boto3.client('s3')


# noinspection PyTypeChecker
def create_api(flask_app):
    from flask_rest_jsonapi import Api

    from app.schemas.garden import GardenList, GardenDetail, GardenBedList, GardenBedDetail
    from app.schemas.bed import BedList, BedDetail, BedPlantList, BedPlantDetail

    from app.schemas.plant import PlantList, PlantDetail
    from app.schemas.plant import PlantNoteList, PlantNoteDetail
    from app.schemas.plant import PlantLightRequirementList, PlantLightRequirementDetail
    from app.schemas.plant import PlantLightRequirementNoteList, PlantLightRequirementNoteDetail
    from app.schemas.plant import PlantWaterRequirementList, PlantWaterRequirementDetail
    from app.schemas.plant import PlantWaterRequirementNoteList, PlantWaterRequirementNoteDetail
    from app.schemas.plant import PlantUseList, PlantUseDetail
    from app.schemas.plant import PlantSeasonList, PlantSeasonDetail
    from app.schemas.plant import PlantPropagationList, PlantPropagationDetail

    from app.schemas.plant_child import PlantChildList, PlantChildDetail
    from app.schemas.lifespan import LifespanList, LifespanDetail
    from app.schemas.soil import SoilList, SoilDetail
    from app.schemas.family import FamilyList, FamilyDetail
    from app.schemas.genus import GenusList, GenusDetail
    from app.schemas.species import SpeciesList, SpeciesDetail
    from app.schemas.category import CategoryList, CategoryDetail
    from app.schemas.measurement_unit import MeasurementUnitList, MeasurementUnitDetail
    from app.schemas.soil_fertility import SoilFertilityList, SoilFertilityDetail
    from app.schemas.growth_habit import GrowthHabitList, GrowthHabitDetail
    from app.schemas.light_requirement import LightRequirementList, LightRequirementDetail
    from app.schemas.water_requirement import WaterRequirementList, WaterRequirementDetail
    from app.schemas.season import SeasonList, SeasonDetail
    from app.schemas.use import UseList, UseDetail
    from app.schemas.note import NoteList, NoteDetail

    api = Api(flask_app)

    api.route(GardenList, 'garden_list', '/gardens')
    api.route(GardenDetail, 'garden_detail', '/gardens/<int:id>')

    api.route(BedList, 'bed_list', '/beds')
    api.route(BedDetail, 'bed_detail', '/beds/<int:id>')

    api.route(LifespanList, 'lifespan_list', '/lifespans')
    api.route(LifespanDetail, 'lifespan_detail', '/lifespans/<int:id>')

    api.route(SoilList, 'soil_list', '/soils')
    api.route(SoilDetail, 'soil_detail', '/soils/<int:id>')

    api.route(FamilyList, 'family_list', '/families')
    api.route(FamilyDetail, 'family_detail', '/families/<int:id>')

    api.route(GenusList, 'genus_list', '/genera')
    api.route(GenusDetail, 'genus_detail', '/genera/<int:id>')

    api.route(SpeciesList, 'species_list', '/species')
    api.route(SpeciesDetail, 'species_detail', '/species/<int:id>')

    api.route(CategoryList, 'category_list', '/categories')
    api.route(CategoryDetail, 'category_detail', '/categories/<int:id>')

    api.route(MeasurementUnitList, 'measurement_unit_list', '/measurement_units')
    api.route(MeasurementUnitDetail, 'measurement_unit_detail', '/measurement_units/<int:id>')

    api.route(SoilFertilityList, 'soil_fertility_list', '/soil_fertility')
    api.route(SoilFertilityDetail, 'soil_fertility_detail', '/soil_fertility/<int:id>')

    api.route(GrowthHabitList, 'growth_habit_list', '/growth_habits')
    api.route(GrowthHabitDetail, 'growth_habit_detail', '/growth_habits/<int:id>')

    api.route(LightRequirementList, 'light_requirement_list', '/light_requirements')
    api.route(LightRequirementDetail, 'light_requirement_detail', '/light_requirements/<int:id>')

    api.route(WaterRequirementList, 'water_requirement_list', '/water_requirements')
    api.route(WaterRequirementDetail, 'water_requirement_detail', '/water_requirements/<int:id>')

    api.route(SeasonList, 'season_list', '/seasons')
    api.route(SeasonDetail, 'season_detail', '/seasons/<int:id>')

    api.route(UseList, 'use_list', '/uses')
    api.route(UseDetail, 'use_detail', '/uses/<int:id>')

    api.route(NoteList, 'note_list', '/notes')
    api.route(NoteDetail, 'note_detail', '/notes/<int:id>')

    api.route(PlantList, 'plant_list', '/plants')
    api.route(PlantDetail, 'plant_detail', '/plants/<int:id>')

    api.route(PlantNoteList, 'plant_note_list', '/plant_notes')
    api.route(PlantNoteDetail, 'plant_note_detail', '/plant_notes/<int:id>')

    api.route(PlantUseList, 'plant_use_list', '/plant_uses')
    api.route(PlantUseDetail, 'plant_use_detail', '/plant_uses/<int:id>')

    api.route(PlantSeasonList, 'plant_season_list', '/plant_seasons')
    api.route(PlantSeasonDetail, 'plant_season_detail', '/plant_seasons/<int:id>')

    api.route(PlantPropagationList, 'plant_propagation_list', '/plant_propagations')
    api.route(PlantPropagationDetail, 'plant_propagation_detail', '/plant_propagations/<int:id>')

    api.route(PlantLightRequirementList, 'plant_light_requirement_list', '/plant_light_requirements')
    api.route(PlantLightRequirementDetail, 'plant_light_requirement_detail', '/plant_light_requirements/<int:id>')

    api.route(PlantLightRequirementNoteList, 'plant_light_requirement_note_list', '/plant_light_requirement_notes')
    api.route(PlantLightRequirementNoteDetail,
              'plant_light_requirement_note_detail', '/plant_light_requirement_notes/<int:id>')

    api.route(PlantWaterRequirementList, 'plant_water_requirement_list', '/plant_water_requirements')
    api.route(PlantWaterRequirementDetail, 'plant_water_requirement_detail', '/plant_water_requirements/<int:id>')

    api.route(PlantWaterRequirementNoteList, 'plant_water_requirement_note_list', '/plant_water_requirement_notes')
    api.route(PlantWaterRequirementNoteDetail,
              'plant_water_requirement_note_detail', '/plant_water_requirement_notes/<int:id>')

    api.route(PlantChildList, 'plant_child_list', '/plant_children')
    api.route(PlantChildDetail, 'plant_child_detail', '/plant_children/<int:id>')

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

s3_bucket = os.getenv('S3_BUCKET')


@application.route("/upload_plant_image", methods=['POST', 'GET'])
def upload():
    s3_filename = str(uuid.uuid4())

    file = request.files['image']

    s3.upload_fileobj(file, s3_bucket, s3_filename, ExtraArgs={'ACL': 'public-read', 'ContentType': file.content_type})

    endpoint = 'https://s3.amazonaws.com/' + s3_bucket + '/' + s3_filename

    return endpoint
