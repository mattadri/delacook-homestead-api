"""empty message

Revision ID: aa64a63f78c8
Revises: d6be1aa64689
Create Date: 2017-07-24 16:46:36.365585

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'aa64a63f78c8'
down_revision = 'd6be1aa64689'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plantgenerationseedcollections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('plant_generation_fk', sa.Integer(), nullable=True),
    sa.Column('date_seeds_harvested', sa.DateTime(), nullable=True),
    sa.Column('total_seeds_harvested', sa.Integer(), nullable=True),
    sa.Column('date_seeds_packaged', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['plant_generation_fk'], ['plantgenerations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('plantgenerations', 'total_seeds_obtained')
    op.drop_column('plantgenerations', 'date_seeds_obtained')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plantgenerations', sa.Column('date_seeds_obtained', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('plantgenerations', sa.Column('total_seeds_obtained', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_table('plantgenerationseedcollections')
    # ### end Alembic commands ###
