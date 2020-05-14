"""empty message

Revision ID: 7e71357051eb
Revises: 99971a0e4318
Create Date: 2020-05-11 19:59:41.717935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e71357051eb'
down_revision = '99971a0e4318'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plant_variety',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('label', sa.String(), nullable=True),
    sa.Column('plant_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['plant_fk'], ['plant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plant_variety')
    # ### end Alembic commands ###
