"""empty message

Revision ID: 8c3b5b99e9a9
Revises: b0bb37d5571b
Create Date: 2021-03-23 14:26:25.562335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c3b5b99e9a9'
down_revision = 'b0bb37d5571b'
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
