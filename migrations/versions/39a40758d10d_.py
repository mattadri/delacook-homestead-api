"""empty message

Revision ID: 39a40758d10d
Revises: ab73a540d0a5
Create Date: 2021-01-24 12:14:40.765094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39a40758d10d'
down_revision = 'ab73a540d0a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('species', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('species', sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
