"""empty message

Revision ID: 1fdd9953c0bf
Revises: 0ae8d80bf4d3
Create Date: 2021-02-01 10:32:48.434912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fdd9953c0bf'
down_revision = '0ae8d80bf4d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('use', sa.Column('is_primary', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('use', 'is_primary')
    # ### end Alembic commands ###
