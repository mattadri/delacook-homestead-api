"""empty message

Revision ID: c066484c0e71
Revises: b94288a31966
Create Date: 2021-03-23 14:33:20.791562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c066484c0e71'
down_revision = 'b94288a31966'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plant', sa.Column('drought_tolerant', sa.Integer(), nullable=True))
    op.add_column('plant', sa.Column('frost_tolerant', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('plant', 'frost_tolerant')
    op.drop_column('plant', 'drought_tolerant')
    # ### end Alembic commands ###