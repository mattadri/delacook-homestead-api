"""empty message

Revision ID: b0bb37d5571b
Revises: c46a23ad0504
Create Date: 2021-03-23 14:25:58.024859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0bb37d5571b'
down_revision = 'c46a23ad0504'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('plant', 'frost_tolerant')
    op.drop_column('plant', 'drought_tolerant')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plant', sa.Column('drought_tolerant', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('plant', sa.Column('frost_tolerant', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
