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
    from app.schemas.plant import PlantingPhysicalSourceList, PlantingPhysicalSourceDetail, PlantingPhysicalSourceRelationship
    from app.schemas.plant import PlantLineageList, PlantLineageDetail, PlantLineageRelationship
    from app.schemas.plant import PlantGenerationList, PlantGenerationDetail, PlantGenerationRelationship
    from app.schemas.plant import PlantLineageGenerationList, PlantLineageGenerationDetail, PlantLineageGenerationRelationship
    from app.schemas.plant import PlantingList, PlantingDetail, PlantingRelationship
    from app.schemas.plant import PlantingNotesList, PlantingNotesDetail, PlantingNotesRelationship
    from app.schemas.plant import PlantGenerationSeedCollectionsList, PlantGenerationSeedCollectionsDetail, PlantGenerationSeedCollectionsRelationship
    from app.schemas.plant import CloningList, CloningDetail, CloningRelationship
    from app.schemas.plant import CloningNotesList, CloningNotesDetail, CloningNotesRelationship
    from app.schemas.plant import PlantHarvestList, PlantHarvestDetail, PlantHarvestRelationship
    from app.schemas.plant import PlantHarvestNotesList, PlantHarvestNotesDetail, PlantHarvestNotesRelationship

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

    api.route(PlantRelationship, 'plant_lineages',
              '/plants/<int:id>/relationships/plantlineages')

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

    api.route(PlantingPhysicalSourceList, 'plantingphysicalsource_list',
              '/plantingphysicalsources')

    api.route(PlantingPhysicalSourceDetail, 'plantingphysicalsource_detail',
              '/plantingphysicalsources/<int:id>')

    api.route(PlantingPhysicalSourceRelationship, 'plantingphysicalsource_plantlineage',
              '/plantingphysicalsources/<int:id>/relationships/plantlineages')

    api.route(PlantLineageList, 'plantlineage_list',
              '/plantlineages',
              '/plants/<int:id>/plantlineages')

    api.route(PlantLineageDetail, 'plantlineage_detail',
              '/plantlineages/<int:id>')

    api.route(PlantLineageRelationship, 'plantlineage_plant',
              '/plantlineages/<int:id>/relationships/plant')

    api.route(PlantLineageRelationship, 'plantlineage_plantingphysicalsource',
              '/plantlineages/<int:id>/relationships/plantingphysicalsource')

    api.route(PlantGenerationList, 'plantgeneration_list',
              '/plantgenerations')

    api.route(PlantGenerationDetail, 'plantgeneration_detail',
              '/plantgenerations/<int:id>')

    api.route(PlantGenerationRelationship, 'plantgeneration_plantlineagegeneration',
              '/plantgenerations/<int:id>/relationships/plantlineagegenerations')

    api.route(PlantLineageGenerationList, 'plantlineagegeneration_list',
              '/plantlineagegenerations')

    api.route(PlantLineageGenerationDetail, 'plantlineagegeneration_detail',
              '/plantlineagegenerations/<int:id>')

    api.route(PlantLineageGenerationRelationship, 'plantlineagegeneration_plantlineage',
              '/plantlineagegenerations/<int:id>/relationships/plantlineages')

    api.route(PlantLineageGenerationRelationship, 'plantlineagegeneration_plantgeneration',
              '/plantlineagegenerations/<int:id>/relationships/plantgeneration')

    api.route(PlantingList, 'planting_list',
              '/plantings')

    api.route(PlantingDetail, 'planting_detail',
              '/plantings/<int:id>')

    api.route(PlantingRelationship, 'planting_plantgeneration',
              '/plantings/<int:id>/relationships/plantgenerations')

    api.route(PlantingRelationship, 'planting_plantingphysicalsource',
              '/plantings/<int:id>/relationships/plantingphysicalsource')

    api.route(PlantingNotesList, 'plantingnote_list',
              '/plantingnotes')

    api.route(PlantingNotesDetail, 'plantingnote_detail',
              '/plantingnotes/<int:id>')

    api.route(PlantingNotesRelationship, 'plantingnote_planting',
              '/plantingnotes/<int:id>/relationships/planting')

    api.route(PlantGenerationSeedCollectionsList, 'plantgenerationseedcollection_list',
              '/plantgenerationseedcollections')

    api.route(PlantGenerationSeedCollectionsDetail, 'plantgenerationseedcollection_detail',
              '/plantgenerationseedcollections/<int:id>')

    api.route(PlantGenerationSeedCollectionsRelationship, 'plantgenerationseedcollection_plantgeneration',
              '/plantgenerationseedcollections/<int:id>/relationships/plantgenerations')

    api.route(CloningList, 'cloning_list',
              '/clonings')

    api.route(CloningDetail, 'cloning_detail',
              '/clonings/<int:id>')

    api.route(CloningRelationship, 'cloning_plantgeneration',
              '/clonings/<int:id>/relationships/plantgenerations')

    api.route(CloningRelationship, 'cloning_plantingphysicalsource',
              '/clonings/<int:id>/relationships/plantingphysicalsource')

    api.route(CloningNotesList, 'cloningnote_list',
              '/cloningnotes')

    api.route(CloningNotesDetail, 'cloningnote_detail',
              '/cloningnotes/<int:id>')

    api.route(CloningNotesRelationship, 'cloningnote_cloning',
              '/cloningnotes/<int:id>/relationships/cloning')

    api.route(PlantHarvestList, 'plantharvest_list',
              '/plantharvests')

    api.route(PlantHarvestDetail, 'plantharvest_detail',
              '/plantharvests/<int:id>')

    api.route(PlantHarvestRelationship, 'harvest_plantgeneration',
              '/plantharvests/<int:id>/relationships/plantgeneration')

    api.route(PlantHarvestNotesList, 'plantharvestnote_list',
              '/plantharvestnotes')

    api.route(PlantHarvestNotesDetail, 'plantharvestnote_detail',
              '/plantharvestnotes/<int:id>')

    api.route(PlantHarvestNotesRelationship, 'harvestnote_harvest',
              '/plantharvestnotes/<int:id>/relationships/plantharvest')


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
