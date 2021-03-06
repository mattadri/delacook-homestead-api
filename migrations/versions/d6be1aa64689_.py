"""empty message

Revision ID: d6be1aa64689
Revises: f0380b03148f
Create Date: 2017-07-24 16:24:29.332091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6be1aa64689'
down_revision = 'f0380b03148f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plantings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('plant_generation_fk', sa.Integer(), nullable=True),
    sa.Column('planting_physical_source_fk', sa.Integer(), nullable=True),
    sa.Column('seeds_started', sa.Integer(), nullable=True),
    sa.Column('date_seeds_started', sa.DateTime(), nullable=True),
    sa.Column('starting_medium', sa.String(), nullable=True),
    sa.Column('seeds_sprouted', sa.Integer(), nullable=True),
    sa.Column('date_first_seeds_sprouted', sa.DateTime(), nullable=True),
    sa.Column('sprouts_planted', sa.Integer(), nullable=True),
    sa.Column('date_sprouts_planted', sa.DateTime(), nullable=True),
    sa.Column('plants_survived', sa.Integer(), nullable=True),
    sa.Column('date_next_generation_seeds_collected', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['plant_generation_fk'], ['plantgenerations.id'], ),
    sa.ForeignKeyConstraint(['planting_physical_source_fk'], ['plantingphysicalsources.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plantingnotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('planting_fk', sa.Integer(), nullable=True),
    sa.Column('note_date', sa.DateTime(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['planting_fk'], ['plantings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plantingnotes')
    op.drop_table('plantings')
    # ### end Alembic commands ###
